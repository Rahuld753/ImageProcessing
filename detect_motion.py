import cv2
import numpy as np

#face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye=cv2.CascadeClassifier('haarcascade_eye.xml')

video=cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2()
while(1):
    ret,frame=video.read()
    fg=fgbg.apply(frame)

    cv2.imshow('fg',fg)


    if(cv2.waitKey(1) & 0xff==ord('q')):
        break;


video.release()
cv2.destroyAllWindows()

