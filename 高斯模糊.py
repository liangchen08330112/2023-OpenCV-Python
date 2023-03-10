#高斯模糊
import cv2
img = cv2.imread("E:\\opencv_img\\nonblur.jpg")
dst = cv2.GaussianBlur(img,(9,9),1)
cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()