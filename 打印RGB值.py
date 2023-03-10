import cv2

img = cv2.imread("D:\\opencv_img\\test06.jpg")
px = img[126,214]  #像素点坐标  [宽度，高度]
print(px)
blue = img[126,214,0]  #第一个通道为蓝色
print(blue)   #打印蓝色通道值
green = img[126,214,1]
print(green)
red = img[126,214,2]
print(red)