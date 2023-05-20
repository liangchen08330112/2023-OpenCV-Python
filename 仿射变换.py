import cv2
import numpy as np

img = cv2.imread("E:\\opencv_img\\paper.jpg")
rows,columns,ch = img.shape
print(img.shape)
pts1=np.float32([[175,103],[35,752],[749,748]])
pts2=np.float32([[44,101],[35,752],[620,748]])
M=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(columns,rows))
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()