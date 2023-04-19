"""
@预测误差计算
@使用四个相邻像素值的几何平均值进行计算
@
@
"""
import tool
import numpy as np
import math
from matplotlib import pyplot as plt
from collections import Counter


#针对黑色区域（即 · 集）进行像素值预测
def black_prediction_error(image):
    #计算图片的宽和高
    width,height = tool.get_w_h(image)
    #获取图片像素值
    pixels = tool.img_to_array(image)
    # 计算 ·集 每个像素的预测误差（分为两部分进行计算， · 集以及 X 集合）
    predictValue = np.zeros((height,width))  # 创建一个大小与图片相同的二维数组，用来存放预测值 p
    # average = np.zeros((height,width))  # 创建一个大小与图片相同的二维数组，用来存放平均数 p'
    predictionError = np.zeros((height,width),dtype=int) # 创建一个大小与图片相同的二维数组，用来存放预测误差值 Pe
    predictionErrorlist = []  #用来存放所有的预测误差值
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if (i + j) % 2 == 0:  # ·集 黑色区域
                a = pixels[i-1][j]
                b = pixels[i][j-1]
                c = pixels[i][j+1]
                d = pixels[i+1][j]
                predictValue[i][j] = math.floor((a*b*c*d)**(1/4))

                predictionError[i][j] = pixels[i][j] - predictValue[i][j]
                predictionErrorlist.append(predictionError[i][j])
    #将预测误差转换为int型数组
    predictionErrorlist = np.array(predictionErrorlist)

    # #计算预测误差值中每个元素出现的个数
    # cishu = Counter(predictionErrorlist)
    # print(type(cishu))
    cishu = tool.count(predictionErrorlist)
    print("区域A各像素出现的次数分别为",cishu)
    # # 绘制预测误差直方图
    # tool.historgrams(predictionErrorlist)
    # # tool.max_min(predictionErrorlist)
    return predictionErrorlist,predictValue


#针对白色区域（即 · 集）进行像素值预测
def white_prediction_error(image):
    #计算图片的宽和高
    width,height = tool.get_w_h(image)
    #获取图片像素值
    pixels = tool.img_to_array(image)
    # 计算 x集 每个像素的预测误差（分为两部分进行计算， · 集以及 X 集合）
    predictValue = np.zeros((height,width))  # 创建一个大小与图片相同的二维数组，用来存放预测值 p
    # average = np.zeros((height,width))  # 创建一个大小与图片相同的二维数组，用来存放平均数 p'
    predictionError = np.zeros((height,width),dtype=int) # 创建一个大小与图片相同的二维数组，用来存放预测误差值 Pe
    predictionErrorlist = []  #用来存放所有的预测误差值
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if (i + j) % 2 != 0:  # x集 白色区域
                a = pixels[i-1][j]
                b = pixels[i][j-1]
                c = pixels[i][j+1]
                d = pixels[i+1][j]
                predictValue[i][j] = (a*b*c*d)**(1/4)
                predictValue[i][j] = math.floor(predictValue[i][j])
                predictionError[i][j] = pixels[i][j] - predictValue[i][j]
                predictionErrorlist.append(predictionError[i][j])
    #将预测误差转换为int型数组
    predictionErrorlist = np.array(predictionErrorlist,dtype=int)

    #计算预测误差值中每个元素出现的个数
    # cishu = Counter(predictionErrorlist)
    # print(type(cishu))
    cishu = tool.count(predictionErrorlist)
    print("区域B各像素出现的次数分别为",cishu)
    # # 绘制预测误差直方图
    # tool.historgrams(predictionErrorlist)
    # tool.max_min(predictionErrorlist)
    return predictionErrorlist,predictValue


