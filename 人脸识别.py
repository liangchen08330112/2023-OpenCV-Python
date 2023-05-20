# 人脸识别
import numpy as np
import cv2
from PIL import Image

print("默认摄像头已启动")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 人脸识别
def getface(img):
    # 人脸识别数据
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # 人眼识别数据
    #eye_cascade=cv2.CascadeClassifier('')
    # 二值化，变为灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # 获取人脸识别数据
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        # 绘画人脸识别数据
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # 根据人脸识别数据添加头像
        img=christmas(img,x,y,w,h)
    return img
def christmas(img,x,y,w,h):
    im=Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    # 你的贴纸地址
    mark=Image.open("crown.png")
    # w是贴纸指定宽度,1024为原始宽度,987是原始高度
    # 987/1024需要依据贴纸实际高、宽进行修改
    height=int(w*987/1024)
    mark=mark.resize((w,height))
    layer=Image.new('RGBA',im.size,(0,0,0,0))
    layer.paste(mark,(x,y-height))
    out=Image.composite(layer,im,layer)
    img=cv2.cvtColor(np.asarray(out),cv2.COLOR_RGB2BGR)
    return img
print("视频写入中...")
videoWriter=cv2.VideoWriter('testwrite.avi',cv2.VideoWriter_fourcc(*'MJPG'),15,(1000,563))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        # 重新定义图片大小
        img=cv2.resize(frame,(1000,563))
        # 添加录像时间
        # img=addtime(img)
        # 实时识别
        img=getface(img)
        # 视频显示
        print("视频已显示")
        cv2.imshow('frame',img)
        # 保存视频
        videoWriter.write(img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            print("您结束了录制")
            break
    else:
        break
cap.release()
print("摄像头已关闭")
videoWriter.release()
print("视频写入停止，视频已保存")
cv2.destroyAllWindows()
print("视频窗口已关闭")