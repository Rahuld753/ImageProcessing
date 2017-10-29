import cv2
import numpy as np

video=cv2.VideoCapture(0)
while(1):
    ret,frame=video.read()
    edges=cv2.Canny(frame,100,100)

    cv2.imshow('edges',edges)

    if(cv2.waitKey(1) & 0xff==ord('q')):
        break;


video.release()
cv2.destroyAllWindows()

