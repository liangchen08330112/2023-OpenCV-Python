import cv2
img = cv2.imread("D:\\opencv_img\\test03.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img',img)
cv2.imshow('gray',gray)
key = cv2.waitKey(0)
if key==27:   #ESC
    print("关闭窗口，不保存处理结果")
    cv2.destroyAllWindows()
elif key==ord('s'):  #S键
    cv2.imwrite('D:\\opencv_img_saving\\test03_gray.png',gray)
    print("关闭窗口，并保存处理结果")
    cv2.destroyAllWindows()