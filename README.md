# Jittor 风景图片生成—边缘引导生成对抗网络在真实感图像合成中的应用

## 简介
| 项目背景、特点

本项目包含了第三届计图挑战赛计图 - 风景图片生成比赛的代码实现。
项目特点：为了改善生成图像的局部细节信息，我们通过对多篇GAN系列文献的比较，最终决定采用基于边缘引导生成对抗网络，也就是ECGAN算法框架来解决赛题。ECGAN的框架图如上图所示，它包括参数共享编码器E、边缘生成器Ge、图像生成器Gi、注意力引导边缘传输模块Gt、标签生成器Gl、相似性损失模块、对比学习模块Gc和多模态鉴别器D等多个关键组件。

#### 运行环境

- python >= 3.7.0
- jittor >= 1.3.8.5

#### 安装依赖

```bash
pip install -r requirements.txt # 本目录下的requirements.txt
```

#### 数据集

请将train_resized文件夹，val_B_labels_resized文件夹放在ECGAN目录中，edge数据集由原训练数据集通过scripts文件夹matlab代码canny.m采集结构特征生成，
edge数据集已经放入train_resized文件中，如果train_resized文件夹中没有edge文件夹，请将edge文件夹放入train_resized文件夹中，放入后文件夹内包含edge，imgs，labels三个文件夹,

预训练模型采用的是 `Jittor` 框架自带的 `vgg19` 模型，无需额外下载，在代码运行的过程中会载入到内存里。

## 训练

在单卡上训练：

```bash
sh train.sh
```
```
bash
CUDA_VISIBLE_DEVICES="0" python train.py --input_path {训练数据集路径（即train_resized文件夹所在路径，train_resized文件夹包含img,labels,edge三个文件夹）}
```
#### 测试

在单卡上进行生成图片：

```bash 
sh test.sh
```
此前需要：
1. 将label与img的映射关系（label_to_img.json）放置在ECGAN目录下
2. 修改test.sh，其内容为：
```
CUDA_VISIBLE_DEVICES="0" python test.py  \
--input_path {测试数据集路径（即labels文件夹所在路径），它提供label mask图} \
--img_path {训练数据集的图片路径（即train_resized/imgs文件夹所在路径，它提供ref图）}\
--ed_path {训练数据集的边缘图片路径（即train_resized/edge文件夹所在路径，它提供edge图）}\
--which_epoch {使用的模型的epoch数目}\
```

#### 生成结果
可点击selects文件夹查看部分生成结果

#### 致谢
此项目基于论文 *EDGE GUIDED GANS WITH CONTRASTIVE LEARNING FOR SEMANTIC IMAGE SYNTHESIS* 实现，部分代码参考了 [jittor-gan](https://github.com/Jittor/gan-jittor)。

#### 注意事项
如果没有edge数据集，那么可以通过scripts文件夹matlab代码canny.m采集原训练数据集结构特征生成
