import onnxruntime as ort
import numpy as np
import cv2
#outcome list
age_list = ['AgeLess18', 'Age18-60', 'AgeOver60']
direct_list = ['Front', 'Side', 'Back']
bag_list = ['HandBag', 'ShoulderBag', 'Backpack']
upper_list = ['UpperStride', 'UpperLogo', 'UpperPlaid', 'UpperSplice']
lower_list = ['LowerStripe', 'LowerPattern', 'LongCoat', 'Trousers', 'Shorts','Skirt&Dress']
#preprocess
def preproc(img, input_size):
    img = img[:, :, ::-1] #BGR to RGB
    img = cv2.resize(img, input_size,interpolation=1) #unified resize
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]
    mean = np.array(mean).reshape((1, 1, 3)).astype('float32') #broadcast
    std = np.array(std).reshape((1, 1, 3)).astype('float32')   #broadcast
    img = (img.astype('float32') * np.float32(1.0/255.0) - mean) / std #normalize scale:1.0/255.0
    img = img.transpose(2, 0, 1).astype('float32') #whc to chw
    return img
x = cv2.imread('img.png') #input 53x163 jpg
x = preproc(x, (192,256)) #w,h
x = x.reshape(1,3,256,192) #batch1
#onnx inference
ort_sess = ort.InferenceSession('model.onnx')
outputs = ort_sess.run(None, {'x': x})
res = outputs[0][0]
print(res)
label = []
#postprocess threshold
threshold=0.5
glasses_threshold=0.3
hold_threshold=0.6
# gender
gender = 'Female' if res[22] > threshold else 'Male'
label.append(gender)
# age
age = age_list[np.argmax(res[19:22])]
label.append(age)
# direction
direction = direct_list[np.argmax(res[23:])]
label.append(direction)
# glasses
glasses = 'Glasses: '
if res[1] > glasses_threshold:
    glasses += 'True'
else:
    glasses += 'False'
label.append(glasses)
# hat
hat = 'Hat: '
if res[0] > threshold:
    hat += 'True'
else:
    hat += 'False'
label.append(hat)
# hold obj
hold_obj = 'HoldObjectsInFront: '
if res[18] > hold_threshold:
    hold_obj += 'True'
else:
    hold_obj += 'False'
label.append(hold_obj)
# bag
bag = bag_list[np.argmax(res[15:18])]
bag_score = res[15 + np.argmax(res[15:18])]
bag_label = bag if bag_score > threshold else 'No bag'
label.append(bag_label)
# upper
upper_res = res[4:8]
upper_label = 'Upper:'
sleeve = 'LongSleeve' if res[3] > res[2] else 'ShortSleeve'
upper_label += ' {}'.format(sleeve)
for i, r in enumerate(upper_res):
    if r > threshold:
        upper_label += ' {}'.format(upper_list[i])
label.append(upper_label)
# lower
lower_res = res[8:14]
lower_label = 'Lower: '
has_lower = False
for i, l in enumerate(lower_res):
    if l > threshold:
        lower_label += ' {}'.format(lower_list[i])
        has_lower = True
if not has_lower:
    lower_label += ' {}'.format(lower_list[np.argmax(lower_res)])

label.append(lower_label)
# shoe
shoe = 'Boots' if res[14] > threshold else 'No boots'
label.append(shoe)

threshold_list = [0.5] * len(res)
threshold_list[1] = glasses_threshold
threshold_list[18] = hold_threshold
pred_res = (np.array(res) > np.array(threshold_list)
            ).astype(np.int8).tolist()
batch_res = []
batch_res.append({"attributes": label, "output": pred_res})
print(batch_res)
