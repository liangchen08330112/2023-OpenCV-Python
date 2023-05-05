import cv2

img = cv2.imread("E:\\opencv_img\\test01.png")
print(img.shape[:2])
cv2.imshow("img",img)
dst=cv2.pyrDown(img)
cv2.imshow("dst",dst)
dst1=cv2.pyrDown(dst)
print(dst1.shape[:2])
cv2.imshow("dst1",dst1)
dst2=cv2.pyrUp(dst1)
print(dst2.shape[:2])
cv2.imshow("dst2",dst2)
dst3=cv2.pyrUp(dst2)
print(dst3.shape[:2])
cv2.imshow("dst3",dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()