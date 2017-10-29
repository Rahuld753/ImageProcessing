import cv2

face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')     #using xml files to detect face and eyes
eye=cv2.CascadeClassifier('haarcascade_eye.xml')

video=cv2.VideoCapture(0)
while(1):
    ret,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face.detectMultiScale(frame,1.3,1)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roig=gray[y:y+h,x:x+w]
        roic=frame[y:y+h,x:x+w]
        eyes=eye.detectMultiScale(roig)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roic,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('facedetect',frame)

    if(cv2.waitKey(1) & 0xff==ord('q')):
        break;


video.release()
cv2.destroyAllWindows()

