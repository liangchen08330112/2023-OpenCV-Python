import cv2
img = cv2.imread("E:\\opencv_img\\zaosheng.jpg")
dst = cv2.medianBlur(img,3)
cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()