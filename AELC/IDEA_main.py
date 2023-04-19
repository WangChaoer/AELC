'''
嵌入步骤：
一、根据白色区域（B）计算黑色区域（A）的波动值
二、根据白色区域（B）计算黑色区域（A）的预测误差
三、将波动值序列进行排序，并将预测误差序列按照波动值序列来排序
四、预测误差值生成预测误差直方图，并寻找两队峰值以及零点值
五、移动直方图
六、嵌入数据
'''
import numpy as np

import IDEA_extract
import tool
import IDEA_embed
import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'
# def main(cover_image,steo_imageA,steo_image,capacity):
# if __name__ == '__main__':
# def main(cover_image,steo_image,reco_image,capacity):
# if __name__ == '__main__':
# def main(capacity):
if __name__ == '__main__':
    cover_image = "./img/plane.tiff"
    steo_image = "./img/steo_image.png"
    reco_image = "./img/reco_image.png"
    capacity  = 10000


    pixels = tool.img_to_array(cover_image)
    locationmap, cpixels = tool.overflow(pixels)
    secret_info = tool.generate_random_number(capacity)
    secretA = secret_info[0:int(len(secret_info)/2)]
    # secretA = np.zeros(50480)
    secretB = secret_info[int(len(secret_info)/2):len(secret_info)]
    # secretB = tool.generate_random_number(33279)
    embedpixA,pk1A,z1A,pk2A,z2A = IDEA_embed.adaptembed_A(cpixels,secretA)
    steopix,pk1B,z1B,pk2B,z2B = IDEA_embed.adaptembed_B(embedpixA,secretB,steo_image)


    pixels = tool.img_to_array(cover_image)
    steopix = tool.img_to_array(steo_image)
    psnr = tool.PSNR(steopix,pixels)
    print(psnr)
    tool.SSIM(steopix,pixels)
    b,recopixelsB = IDEA_extract.extract_B(steo_image,pk1B,z1B,pk2B,z2B,len(secretB))
    a = IDEA_extract.extract_A(recopixelsB,pk1A,z1A,pk2A,z2A,len(secretA),reco_image,locationmap)


    if (secretB != b ).any() :
        print("b提取失败")
    if (secretA != a ).any() :
        print("a提取失败")
    recover = tool.img_to_array(reco_image)
    pixels = tool.img_to_array(cover_image)
    if (recover != pixels).any():
        print("恢复失败")

# cover_image = ["./img/lena.tiff","./img/plane.tiff","./img/man.tiff","./img/baboon.tiff","./img/boat.tiff","./img/elaine.tiff"]
# steo_image = ["./img/lenasteo.png","./img/planesteo.png","./img/mansteo.png","./img/baboonsteo.png","./img/boatsteo.png","./img/elainesteo.png"]
# reco_image = ["./img/recolena.png","./img/recoplane.png","./img/recoman.png","./img/recobaboon.png","./img/recoboat.png","./img/recoelaine.png"]
# capacity = [2622,5243,7865,10486,13108,15729,18351,20972,23593,26215,28836,31458,34079,36701]
# for i in range(3):
#     for j in range(14):
#         main(cover_image[i],steo_image[i],reco_image[i],capacity[j])
# capacity = [2500,5000,7500,10000,12500,15000,17500,20000,22500,25000,27500,30000,32500,35000,37500,40000,42500,45000]
# capacity = [2000,4000,6000,8000,10000,12000,14000,16000,18000,20000]
# capacity = [2500,5000,7500,10000,12500,15000,17500,20000,22500,25000,27500,30000]
# for i in range(12):
#     main(capacity[i])