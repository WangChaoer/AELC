'''
@方差以及波动值计算
@实验部分
@主要内容：计算像素值的方差，并在方差的基础上计算除第一行和最后一行以及第一列和最后一列像素的波动值
'''
import numpy as np
import cv2
import tool

#计算方差
def calculate_variance (pixels):
    #计算图片的宽和高
    width,height = len(pixels[0]),len(pixels)
    #获取图片像素值
    # 计算每个像素的方差（所有像素值均需计算）
    variance = np.zeros((height,width))  # 创建一个大小与图片相同的二维数组，用来存放方差 S
    average = np.zeros((height,width))  # 创建一个大小与图片相同的二维数组，用来存放平均数 x‘
    for i in range(height):  # 行
        for j in range(width):  # 列
            if i == 0:  # 第一行三种情况
                if j == 0:
                    average[i][j] = (pixels[i][j + 1] + pixels[i + 1][j]) / 2
                    variance[i][j] = ((pixels[i][j + 1] - average[i][j]) ** 2 + (pixels[i + 1][j] - average[i][j]) ** 2) / 2
                elif j == width - 1:
                    average[i][j] = (pixels[i][j - 1] + pixels[i + 1][j]) / 2
                    variance[i][j] = ((pixels[i][j - 1] - average[i][j]) ** 2 + (pixels[i + 1][j] - average[i][j]) ** 2) / 2
                else:
                    average[i][j] = (pixels[i][j - 1] + pixels[i][j + 1] + pixels[i + 1][j]) / 3
                    variance[i][j] = ((pixels[i][j - 1] - average[i][j]) ** 2 + (pixels[i][j + 1] - average[i][j]) ** 2 + (pixels[i + 1][j] - average[i][j]) ** 2) / 3

            elif i == height - 1:  # 最后一行三种情况
                if j == 0:
                    average[i][j] = (pixels[i - 1][j] + pixels[i][j + 1]) / 2
                    variance[i][j] = ((pixels[i - 1][j] - average[i][j]) ** 2 + (pixels[i][j + 1] - average[i][j]) ** 2) / 2
                elif j == width - 1:
                    average[i][j] = (pixels[i - 1][j] + pixels[i][j - 1]) / 2
                    variance[i][j] = ((pixels[i - 1][j] - average[i][j]) ** 2 + (pixels[i][j - 1] - average[i][j]) ** 2) / 2
                else:
                    average[i][j] = (pixels[i][j - 1] + pixels[i][j + 1] + pixels[i - 1][j]) / 3
                    variance[i][j] = ((pixels[i][j - 1] - average[i][j]) ** 2 + (pixels[i][j + 1] - average[i][j]) ** 2 + (pixels[i - 1][j] - average[i][j]) ** 2) / 3

            else:  # 中间行的三种情况
                if j == 0:
                    average[i][j] = (pixels[i - 1][j] + pixels[i + 1][j] + pixels[i][j + 1]) / 3
                    variance[i][j] = ((pixels[i - 1][j] - average[i][j]) ** 2 + (pixels[i + 1][j] - average[i][j]) ** 2 + (pixels[i][j + 1] - average[i][j]) ** 2) / 3
                elif j == width - 1:
                    average[i][j] = (pixels[i - 1][j] + pixels[i + 1][j] + pixels[i][j - 1]) / 3
                    variance[i][j] = ((pixels[i - 1][j] - average[i][j]) ** 2 + (pixels[i + 1][j] - average[i][j]) ** 2 + (pixels[i][j - 1] - average[i][j]) ** 2) / 3
                else:
                    average[i][j] = (pixels[i - 1][j] + pixels[i + 1][j] + pixels[i][j - 1] + pixels[i][j + 1]) / 4
                    variance[i][j] = ((pixels[i - 1][j] - average[i][j]) ** 2 + (pixels[i + 1][j] - average[i][j]) ** 2 + (pixels[i][j - 1] - average[i][j]) ** 2 + (pixels[i][j + 1] - average[i][j]) ** 2) / 4
    return variance

#计算黑色集（A集 ·集）每个像素的波动值（除去第一行第一列以及最后一行最后一列）
def black_calculate_fluctuated_value(pixels):
    #计算图片的宽和高
    width,height = len(pixels[0]),len(pixels)
    #获取图像每个像素点的方差
    variance = calculate_variance(pixels)
    #波动值数组的定义（不计算第一行和最后一行以及第一列和最后一列）
    flucatedValue = np.zeros((height,width))
    #波动值的计算（不计算第一行和最后一行以及第一列和最后一列）
    flucatedValueList = []
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if (i + j) % 2 == 0:
                # flucatedValue[i][j] = variance[i][j] + (variance[i-1][j-1] + variance[i-1][j+1] + variance[i+1][j-1] + variance[i+1][j+1])/4
                # flucatedValue[i][j] = variance[i][j]
                flucatedValue[i][j] = (variance[i][j] +
                            variance[i - 1][j - 1] + variance[i - 1][j + 1] + variance[i + 1][j - 1] + variance[i + 1][
                        j + 1]) / 5
                flucatedValueList.append(flucatedValue[i][j])
    flucatedValueList = np.array(flucatedValueList)
    # print(flucatedValue)
    return flucatedValueList

#计算白色集（B集 x集）每个像素的波动值（除去第一行第一列以及最后一行最后一列）
def white_calculate_fluctuated_value(pixels):
    #计算图片的宽和高
    width,height = len(pixels[0]),len(pixels)
    #获取图像每个像素点的方差
    variance = calculate_variance(pixels)
    #波动值数组的定义（不计算第一行和最后一行以及第一列和最后一列）
    flucatedValue = np.zeros((height,width))
    #波动值的计算（不计算第一行和最后一行以及第一列和最后一列）
    flucatedValueList = []
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if (i + j) % 2 != 0:
                # flucatedValue[i][j] = variance[i][j] + (variance[i-1][j-1] + variance[i-1][j+1] + variance[i+1][j-1] + variance[i+1][j+1])/4
                # flucatedValue[i][j] = variance[i][j]
                flucatedValue[i][j] = (variance[i][j] +
                            variance[i - 1][j - 1] + variance[i - 1][j + 1] + variance[i + 1][j - 1] + variance[i + 1][
                        j + 1]) / 5
                flucatedValueList.append(flucatedValue[i][j])
    flucatedValueList = np.array(flucatedValueList)
    # print(flucatedValue)
    return flucatedValueList