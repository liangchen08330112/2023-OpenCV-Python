import cv2

img = cv2.imread("E:\\opencv_img\\SuperMario.jpg")
res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)
height,width = img.shape[:2]
res2 = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_LINEAR)

while(1):
    cv2.imshow('res',res)
    cv2.imshow('img',img)
    cv2.imshow('res2',res2)
    if cv2.waitKey(1) & 0xFF==27:
        break

cv2.destroyAllWindows()