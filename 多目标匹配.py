#多目标匹配
import cv2
import numpy as np

img_rgb = cv2.imread("E:\\opencv_img\\SuperMario.jpg")
gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template = cv2.imread("E:\\opencv_img\\Mario.jpg",0)

print(template.shape)
w,h = template.shape[::-1]
print(w)
print(h)
res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
threshold =0.8
loc = np.where(res>=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)
cv2.imshow('res',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()