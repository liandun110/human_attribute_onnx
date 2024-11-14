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

#预测结果
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