#自适应阈值
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("E:\\opencv_img\\adaptive.jpg",0)

# 中值滤波：去除噪点
img = cv2.medianBlur(img,5)
ret, threshold1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
threshold2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY,11,2)
threshold3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,
                                   11,2)
titles = ['Original','Global Threshing (v=127)','Adaptive Mean Threshing','Adaptive Gaussian Threshing']
imgs = [img,threshold1,threshold2,threshold3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()