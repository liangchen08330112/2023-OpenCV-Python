#lun kuo jin si
import cv2
img = cv2.imread("D:\photos\shape.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,190,255,cv2.THRESH_BINARY_INV)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours_show = cv2.drawContours(img,contours,-1,(255,143,34),3)
print(len(contours))
for i in range(len(contours)):
    epsilon = 0.01*cv2.arcLength(contours[i],True)
    approx = cv2.approxPolyDP(contours[i],epsilon,True)    #轮廓逼近
    print(len(approx))
    if(len(approx)==3):
        print("第",i,"条轮廓是三角形")
    if(len(approx)==4):
        print("第",i,"条轮廓是矩形")
    if(len(approx)==10):
        print("第",i,"条轮廓是五角星")
    if(len(approx)==16):
        print("第",i,"条轮廓是圆形")

cv2.imshow('gray',gray)
cv2.imshow('thresh',thresh)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()