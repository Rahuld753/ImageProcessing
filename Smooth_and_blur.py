#using skin_color_detection.py and providing blur and smooth effect in it

import cv2
import numpy as np

video=cv2.VideoCapture(0)
while(1):
    ret,frame=video.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower=np.array((0,48,80))
    upper=np.array((20,255,255))

    mask=cv2.inRange(hsv,lower,upper)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    kernel=np.ones((15,15),np.float32)/225
    smoothed=cv2.filter2D(res,-1,kernel)           #providing smoothening effect
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)   #providing laplacian effect

    blur=cv2.GaussianBlur(res,(15,15),0)           #providing blurring effect


    cv2.imshow('smooth',smoothed)
    cv2.imshow('blur',blur)
    cv2.imshow('laplacian',laplacian)



    if(cv2.waitKey(1) & 0xff==ord('q')):
        break;


video.release()
cv2.destroyAllWindows()

