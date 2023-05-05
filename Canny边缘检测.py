import cv2

def edge_demo(img):
    blurred = cv2.GaussianBlur(img,(3,3),0)
    gray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
    edge_output = cv2.Canny(gray,50,150)
    dst = cv2.bitwise_and(img,img,mask=edge_output)
    cv2.imshow("Canny Edge", edge_output)
    cv2.imshow("Color Edge", dst)

src=cv2.imread('D:/photos/bianyuan.jpg')
cv2.imshow('input image',src)
edge_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
