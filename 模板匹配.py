#模板匹配
import cv2
src = cv2.imread("D:/photos/bai.jpg")
img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
#读入小的模板图像
template = cv2.imread("D:/photos/suoxiao.jpg",0)
#print(template.shape)
w,h = template.shape
print(w)
print(h)
cv2.imshow( "img" ,img)
cv2.imshow("template " ,template)
#All the 6 methods for comparison in a list
methods = [ 'cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
'cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED ']
for meth in methods:
    img2 = img.copy()
    method = eval(meth)
    print(meth)
    print(method)
    res = cv2.matchTemplate(img2, template,method)
    min_val,max_val, min_loc,max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        print(top_left)
    else:
        top_left = max_loc
        print(top_left)
    bottom_right = (top_left[0] +h, top_left[1] + w)
    src1=src.copy()
    cv2.rectangle(src1,top_left, bottom_right,(0,0,255),2)
    cv2.imshow(meth ,src1)
cv2.waitKey(0)
cv2.destroyAllWindows()