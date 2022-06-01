# Facial-Expression-Recognition-Based-on-Attention-Mechanism
基于注意力机制的表情识别
### 文件目录解释
#### 1. Dataset  
用来存放数据集
#### 2. Models  
用来存放的模型，可以是已有的Paddle格式的模型
#### 3. Pages  
- assets 用到的图片资源
- assets.qrc 使用PySide生成的样式文件
- assets_rc.py GUI界面的样式文件，此目录和根目录都有，我忘记是调用的哪一个了，所以都保留了。
#### 4. Train  
训练时的工作路径，自行训练的模型会保存在这里
#### 5. Utils
- AttResNet.py 网络代码
- DatasetProcess.py 数据集处理代码
- FaceDetection.py 人脸检测代码
- Predict.py 模型预测代码
- VisualTrain.py 模型训练代码  
- CSV文件 用来保存数据集和创建的信息
### 注意事项  
* #### 配置好环境，安装使用PySide的工具，不会安装见如下以PyCharm为例的说明  
1. 依次点击 File:arrow_right:Settings:arrow_right:Tools:arrow_right:External Tools:arrow_right::heavy_plus_sign:添加PySide工具,工具所在的目录为 _你的Python环境_ \Scripts  
2. 分别添加 _pyside6-designer.exe_ 、 _pyside6-rcc.exe_ 和 _pyside6-uic.exe_ 三个工具，Arguments和Working directory参数分别均为 _\$FileName\$ -o \$FileNameWithoutExtension\$.py_ 和 _\$FileDir\$_
* #### GUI界面的操作顺序尽量规范，可参考该[视频](https://www.bilibili.com/video/BV1mY411u7ia?share_source=copy_web)  ~~禁止白嫖~~
* #### 我的代码特别脆弱，不知道别人能不能完全看懂，所以请谨慎改动，当然，如果您是大佬，请随意发挥。
* #### 模型目前默认识别7个分类，如需修改请在 _AttResNet.py_ 中调整 _num_classes_ 参数即可
* #### Notebook项目和数据集见[我在AI Studio上获得黄金等级，点亮3个徽章，来互关呀~ ](https://aistudio.baidu.com/aistudio/personalcenter/thirdview/774657)
* #### ~~禁止白嫖~~ ~~禁止白嫖~~ ~~禁止白嫖~~ 















