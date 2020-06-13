# Face-recognition-for-classroom-sign-in
基于FaceNet的人脸检测+识别的课堂学生签到系统

更多项目请关注我的博客：https://blog.csdn.net/weixin_44936889

# 展示：

注：
开头两个裁判没加到数据库，用作负样本展示；

AND 开头稍长，请耐心看完hahh，后面还是挺有意思的一个小视频。

![image](https://github.com/Sharpiless/Face-recognition-for-classroom-sign-in/blob/master/dst.gif)

# 界面图 ：

## 1. 人脸数据库采集界面：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528080406789.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_80,color_FFFFFF,t_0)

## 2. 人脸签到界面：
（可载入本地视频或者摄像头实时视频）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528080532336.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_80,color_FFFFFF,t_100)

# 算法简介：
该模块通过卷积神经网络将人脸图像映射为一个一维的特征向量，任何对比检测人脸特征和数据库中人脸的特征在特征空间的距离，从而计算人脸相似度并进行人脸匹配和识别，其基本流程为：

 - 使用MTCNN检测人脸区域并进行裁剪；
 - 使用FaceNet模型直接将人脸图像转换到特征空间的一维特征向量。即通过一个深度的卷积神经网络，利用卷积层和池化层进行高层特征计算和下采样得到特征向量，这些特征向量的空间距离的长度就代表了特征的相似度，从而能够进行人脸匹配；
 - 得到检测人脸的特征向量后，通过计算该人脸的特征向量与数据库中已经计算的人脸特征的距离来匹配人脸，并设置阙值来过滤陌生人脸；
 
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528080917104.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_80,color_FFFFFF,t_0)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528080845834.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_80,color_FFFFFF,t_0)

# 总结：
本文调研并比对了不同人脸识别方法，重点介绍了本文开发的基于FaceNet的人脸识别系统的原理。

并且本文基于FaceNet开发了一套完整可行的人脸识别系统，功能包括：截取实时视频，检测和切割人脸图片，人脸特征匹配和识别等。

权重文件需要的请私戳作者~

联系我时请备注所需模型权重，我会拉你进交流群~

该群会定时分享各种源码和模型，之前分享过的请从群文件中下载~

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200613141749103.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)
