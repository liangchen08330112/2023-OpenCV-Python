import cv2

shape1 = cv2.imread("E:\\opencv_img\\shape1.png",0)
shape2 = cv2.imread("E:\\opencv_img\\shape2.png",0)
shape3 = cv2.imread("E:\\opencv_img\\shape3.png",0)

ret1,thresh1 = cv2.threshold(shape1,150,255,cv2.THRESH_BINARY_INV)
ret2,thresh2 = cv2.threshold(shape2,150,255,cv2.THRESH_BINARY_INV)
ret3,thresh3 = cv2.threshold(shape3,250,255,cv2.THRESH_BINARY_INV)

contours1,hierarchy1=cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours2,hierarchy2=cv2.findContours(thresh2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours3,hierarchy3=cv2.findContours(thresh3,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

c1 = contours1[0]
c2 = contours2[0]
c3 = contours3[0]

help(cv2.matchShapes)
r1 = cv2.matchShapes(c1,c3,cv2.CONTOURS_MATCH_I1,0.0)
r2 = cv2.matchShapes(c3,c2,cv2.CONTOURS_MATCH_I1,0.0)

print("图3和图1的相似度为：",r1)
print("图3和图2的相似度为：",r2)

cv2.imshow("shape1",shape1)
cv2.imshow("shape2",shape2)
cv2.imshow("shape3",shape3)
cv2.imshow("thresh1",thresh1)
cv2.imshow("thresh2",thresh2)
cv2.imshow("thresh3",thresh3)

cv2.waitKey(0)
cv2.destroyAllWindows()