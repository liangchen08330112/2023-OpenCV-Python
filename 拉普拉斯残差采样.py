import cv2 as cv

src = cv.imread("E:\\opencv_img\\peppapig.jpg")
#src = cv.imread("D:\\Projects\\Python\\pig.jpg")
print(src.shape[:2])

# 高斯金字塔第 0 层
gus0 = src  # 原图
# 高斯金字塔第 1 层
gus1 = cv.pyrDown(gus0)
print(gus1.shape[:2])
# 高斯第 2 层
gus2 = cv.pyrDown(gus1)
print(gus2.shape[:2])

#图像减法求差异
# 拉普拉斯金字塔第 0 层
lap0 = gus0 - cv.pyrUp(gus1)
# 拉普拉斯金字塔第 1 层
lap1 = gus1 - cv.pyrUp(gus2)

rep = lap0 + cv.pyrUp(lap1 + cv.pyrUp(gus2))
gus_rep = cv.pyrUp(cv.pyrUp(gus2))

cv.imshow("src", src)
cv.imshow("rep", rep)
cv.imshow("gus_rep", gus_rep)
cv.waitKey()