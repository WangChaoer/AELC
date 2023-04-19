
"""
@预测误差计算
@
@
@
"""
import tool

import numpy as np
import math
from matplotlib import pyplot as plt
from collections import Counter


#针对黑色区域（即 · 集）进行像素值预测
def black_prediction_error(pixels):
    #计算图片的宽和高
    width,height = len(pixels[0]),len(pixels)

    # 计算 ·集 每个像素的预测误差（分为两部分进行计算， · 集以及 X 集合）
    predictValue = np.zeros((height,width))  # 创建一个大小与图片相同的二维数组，用来存放预测值 p
    # average = np.zeros((height,width))  # 创建一个大小与图片相同的二维数组，用来存放平均数 p'
    predictionError = np.zeros((height,width),dtype=int) # 创建一个大小与图片相同的二维数组，用来存放预测误差值 Pe
    predictionErrorlist = []  #用来存放所有的预测误差值
    dv = np.zeros(4)
    w1 = np.zeros(4)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if (i + j) % 2 == 0:  # ·集 黑色区域
                a = pixels[i-1][j]
                b = pixels[i][j-1]
                c = pixels[i][j+1]
                d = pixels[i+1][j]
                ave = ((a+b+c+d)/4)
                dv[0] = abs(ave-a)
                dv[1] = abs(ave-b)
                dv[2] = abs(ave-c)
                dv[3] = abs(ave-d)
                sum_dv = sum(dv)
                if sum_dv == 0 :
                    w1[:] = 0.25
                else:
                    for r in range(len(dv)):
                        w1[r] = (sum_dv / (1+dv[r]))
                w = tool.normalization4(w1)
                predictValue[i][j] = math.floor((a**w[0]*b**w[1]*c**w[2]*d**w[3]))
                # predictValue[i][j] = math.floor(((a * b * c* d) ** 0.25))
                predictionError[i][j] = pixels[i][j] - predictValue[i][j]
                predictionErrorlist.append(predictionError[i][j])
    #将预测误差转换为int型数组
    predictionErrorlist = np.array(predictionErrorlist)

    # # #计算预测误差值中每个元素出现的个数
    # cishu = Counter(predictionErrorlist)
    # print(type(cishu))
    # 计算预测误差为(-3,2]出现的次数
    # cishu = tool.count(predictionErrorlist)
    # print(cishu)
    # print(cishu[-1][1]+cishu[-2][1])
    # num=0
    # for i in range(0,len(cishu)):
    #     if cishu[i][0]>(-3) and cishu[i][0]<=2:
    #         num=num+cishu[i][1]
    # print(num)

    # # 绘制预测误差直方图
    # tool.historgrams(predictionErrorlist)
    # # # tool.max_min(predictionErrorlist)
    # return predictionErrorlist
    # MaxPix,MaxPoint,To_MaxPoint_min_Point,Second_MaxPix,Second_MaxPoint,To_SecondMaxPoint_min_Point=tool.max_and_min(predictionErrorlist,1)
    # print(MaxPix, MaxPoint, To_MaxPoint_min_Point, Second_MaxPix, Second_MaxPoint, To_SecondMaxPoint_min_Point)
    return predictionErrorlist,predictValue
pixels = tool.img_to_array("../img/yinzhaoxia/man.tiff")
black_prediction_error(pixels)

def white_prediction_error(pixels):
    #计算图片的宽和高
    width,height = len(pixels[0]),len(pixels)

    # 计算 x集 每个像素的预测误差（分为两部分进行计算， · 集以及 X 集合）
    predictValue = np.zeros((height,width))  # 创建一个大小与图片相同的二维数组，用来存放预测值 p
    # average = np.zeros((height,width))  # 创建一个大小与图片相同的二维数组，用来存放平均数 p'
    predictionError = np.zeros((height,width),dtype=int) # 创建一个大小与图片相同的二维数组，用来存放预测误差值 Pe
    predictionErrorlist = []  #用来存放所有的预测误差值
    dv = np.zeros(4)
    w1 = np.zeros(4)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if (i + j) % 2 != 0:  # ·集 黑色区域
                a = pixels[i-1][j]
                b = pixels[i][j-1]
                c = pixels[i][j+1]
                d = pixels[i+1][j]
                ave = ((a+b+c+d)/4)
                dv[0] = abs(ave-a)
                dv[1] = abs(ave-b)
                dv[2] = abs(ave-c)
                dv[3] = abs(ave-d)
                sum_dv = sum(dv)
                if sum_dv == 0 :
                    w1[:] = 0.25
                else:
                    for r in range(len(dv)):
                        w1[r] = (sum_dv / (1+dv[r]))
                w = tool.normalization4(w1)
                predictValue[i][j] = math.floor((a**w[0]*b**w[1]*c**w[2]*d**w[3]))
                predictionError[i][j] = pixels[i][j] - predictValue[i][j]
                predictionErrorlist.append(predictionError[i][j])
    #将预测误差转换为int型数组
    predictionErrorlist = np.array(predictionErrorlist)

    #计算预测误差值中每个元素出现的个数
    # cishu = Counter(predictionErrorlist)
    # print(type(cishu))
    # cishu = tool.count(predictionErrorlist)
    # print(cishu)
    # print("区域B各像素出现的次数分别为",cishu)
    # # 绘制预测误差直方图
    # tool.historgrams(predictionErrorlist)
    # tool.max_min(predictionErrorlist)
    # 计算预测误差为(-3,2]出现的次数
    # cishu = tool.count(predictionErrorlist)
    # num=0
    # for i in range(0,len(cishu)):
    #     if cishu[i][0]>(-3) and cishu[i][0]<=2:
    #         num=num+cishu[i][1]
    # print(num)

    return predictionErrorlist,predictValue

