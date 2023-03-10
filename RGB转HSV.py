# RGB转HSV
import cv2
img = cv2.imread("D:\\opencv_img\\test03.jpg")
cv2.imshow('img',img)
# cvtColor是OpenCV的颜色模型转换函数。img表示需要转换的图片，COLOR_BGR2HSV表示RGB转HSV。
# 但是HSV图像显示出来颜色会很奇怪，所以它并不是很适合作为显示器的模型。但它适合用于追踪某个颜色。
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)
cv2.waitKey(10000)
# cv2.imwrite("D:\\opencv_img_saving\\test03_hsv.jpg",hsv)
# print("HSV图片已保存")
cv2.destroyAllWindows()
