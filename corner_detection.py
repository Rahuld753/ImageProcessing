import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('imag.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #converting bgr to grayscale
gray=np.float32(gray)

corners=cv2.goodFeaturesToTrack(gray,10,0.01,10)      #detecting the corners
corners=np.int0(corners)

for c in corners:
    x,y=c.ravel()
    cv2.circle(img,(x,y),5,0,2)     #use small cirle to mark corners

plt.imshow(img)
plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()