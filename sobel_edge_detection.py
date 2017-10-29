import cv2
import numpy as np

video=cv2.VideoCapture(0)
while(1):
    ret,frame=video.read()
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)

    if(cv2.waitKey(1) & 0xff==ord('q')):
        break;


video.release()
cv2.destroyAllWindows()

