#二值化
import cv2

img = cv2.imread("E:\\opencv_img\\erzhihua.jpg")
cv2.imshow('img',img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

threshold = cv2.threshold(gray,115,255,cv2.THRESH_BINARY,gray)
cv2.imshow('threshold',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()