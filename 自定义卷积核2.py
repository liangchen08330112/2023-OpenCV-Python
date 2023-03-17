import cv2
import numpy as np

img = cv2.imread("E:\\opencv_img\\gezi.jpg")
#自定义卷积核
#水平方向
kernel = np.array([[-1,-1,-1],
                   [0 , 0, 0],
                   [1 , 1, 1]])
#垂直方向
kernel2 = np.array([[-1, 0,1],
                   [-1 , 0,1],
                   [-1 , 0,1]])
dst = cv2.filter2D(img,-1,kernel)  #滤波
dst2 = cv2.filter2D(img,-1,kernel2)  #滤波
cv2.imshow('img',img)
cv2.imshow('After',dst)
cv2.imshow('After2',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()