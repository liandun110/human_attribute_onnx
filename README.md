# 安装依赖
```bash
conda create -n human_attribute_onnx python=3.10.15
conda activate human_attribute_onnx
pip install -r requirements.txt
```

# 使用步骤

```bash
python demo.py
```

# 预测结果
- 性别：男、女
- 年龄：小于18、18-60、大于60
- 朝向：朝前、朝后、侧面
- 配饰：眼镜、帽子、无
- 正面持物：是、否
- 包：双肩包、单肩包、手提包
- 上衣风格：带条纹、带logo、带格子、拼接风格
- 下装风格：带条纹、带图案
- 短袖上衣：是、否
- 长袖上衣：是、否
- 长外套：是、否
- 长裤：是、否
- 短裤：是、否
- 短裙&裙子：是、否
- 穿靴：是、否

# 调研
## 行人属性识别其实是一个多标签图像分类问题
本工程参考：https://blog.csdn.net/weixin_43945848/article/details/128565601
https://gitcode.com/gh_mirrors/pa/Paddle2ONNX/overview?utm_source=highlight_word_gitcode&word=paddle2onnx&isLogin=1
https://github.com/PaddlePaddle/PaddleClas

算法一：APTM(ACM MM 2023): https://github.com/Shuyu-XJTU/APTM
无onnx相关代码，有训练步骤

算法二：Label2Label(ECCV2022)：https://github.com/Li-Wanhua/Label2Label

无evaluation.py、onnx相关代码，有训练步骤，无可视化

算法三：VTFPAR++：https://github.com/Event-AHU/OpenPAR/tree/main/VTFPAR%2B%2B

有demo演示，有训练过程

算法四：PromptPAR：https://github.com/Event-AHU/OpenPAR/tree/main/PromptPAR

无demo

算法五：mambaPAR：https://github.com/EventAHU/OpenPAR/tree/main/MambaPAR_Empirical_Study

无测试代码，mamba不好搞

算法六：SequencePAR：https://github.com/Event-AHU/OpenPAR/tree/main/SequencePAR

无demo