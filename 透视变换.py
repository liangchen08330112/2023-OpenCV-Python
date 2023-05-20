import cv2
import numpy as np
# 透视变换矫正照片
img = cv2.imread('E:\\opencv_img\\paper.jpg')
rows,columns,ch = img.shape
print(img.shape)
pts1=np.float32([[175,103],[604,111],[35,752],[749,748]])
pts2=np.float32([[44,101],[749,112],[35,752],[749,748]])

M=cv2.getPerspectiveTransform(pts1,pts2)

dst=cv2.warpPerspective(img,M,(columns,rows))
cv2.imshow("dst",dst)
cv2.imshow("original",img)
cv2.waitKey()
cv2.destroyAllWindows()