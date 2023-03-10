#均值模糊
import cv2
img = cv2.imread("E:/opencv_img/nonblur.jpg")
dst = cv2.blur(img,(3,3))
cv2.imshow('img',img)
cv2.imshow('dst2',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()