#轮廓拟合
import cv2
import numpy as np

img = cv2.imread("E:\\opencv_img\\shape.png")
cv2.imshow("img",img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

ret,threshold = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
cv2.imshow("threshold",threshold)

#contours,hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours,hierarchy = cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#ontours,hierarchy = cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img,contours,-1,(255,56,251),2)
cv2.imshow("img2",img)
cv2.waitKey(0)
cv2.destroyAllWindows()