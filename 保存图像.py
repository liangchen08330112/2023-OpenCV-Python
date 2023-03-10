# 保存图像
import cv2

img = cv2.imread("D:\\opencv_img\\test06.jpg")
cv2.imshow("test06",img)
key = cv2.waitKey(0)
if key==27:   #ESC
    print("ESC键：关闭窗口，不保存图像")
    cv2.destroyAllWindows()
elif key==ord('s'):  #S键
    cv2.imwrite('D:\\opencv_img_saving\\test06_save.jpg',img)
    print("S键：关闭窗口，并保存图像")
    cv2.destroyAllWindows()