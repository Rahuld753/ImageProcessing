import cv2
import numpy as np


video=cv2.VideoCapture(0)             #capture your webcam as video feed using 0 as parameter
while(1):
    ret,frame=video.read()              #video.read() returns true,the webcam frame window
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)     #converting from BGR to HSV color model

    lower=np.array((0,48,80))                    #specifying the lower range for skin color
    upper=np.array((20,255,255))                 #specifying the upper range for skin color

    mask=cv2.inRange(hsv,lower,upper)            #masking the specified color area with white color
    res=cv2.bitwise_and(frame,frame,mask=mask)   #giving actual color of masked area

    cv2.imshow('mask',mask)
    cv2.imshow('res',res)                        #to show video frame providing title and the frame as parameters in imshow()


    if(cv2.waitKey(1) & 0xff==ord('q')):         #press q to exit
        break;


video.release()                                 #release the captured video
cv2.destroyAllWindows()                         #destroy all windows

