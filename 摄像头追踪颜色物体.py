#摄像头追踪颜色物体
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
    # 获取每一帧
    ret,frame=cap.read()
    # BGR转HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # 设定红色的阈值
    lower_red=np.array([0,43,46])
    upper_red=np.array([10,255,255])
    #根据阈值构建掩模
    mask=cv2.inRange(hsv,lower_red,upper_red)
    #对原图像和掩模进行位运算
    res=cv2.bitwise_and(frame,frame,mask=mask)
    #显示图像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:  # 按下ESC关闭视频
        break
cap.release()
print("退出视频")
cv2.destroyAllWindows()