# RGB通道分离与合并
import cv2
img = cv2.imread("D:\\opencv_img\\test03.jpg")
b,g,r = cv2.split(img)  #分离函数
merged = cv2.merge([b,g,r])
# 显示图像
cv2.imshow('image',img)
cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red',r)
cv2.imshow('Merged',merged)
cv2.waitKey(0)
# 保存处理结果
cv2.imwrite("E:\\opencv_img_saving\\test03_blue.jpg",b)
cv2.imwrite("E:\\opencv_img_saving\\test03_green.jpg",g)
cv2.imwrite("E:\\opencv_img_saving\\test03_red.jpg",r)
cv2.imwrite("E:\\opencv_img_saving\\test03_merged.jpg",merged)
cv2.destroyAllWindows()