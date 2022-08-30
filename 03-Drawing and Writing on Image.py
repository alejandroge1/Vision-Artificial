import numpy as np
import cv2

img = cv2.imread(r'C:\Users\skinl\Pictures\carro.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(50,30),(0,0,255),5)

cv2.rectangle(img,(50,25),(150,50),(0,0,0),2)
cv2.circle(img,(70,140), 60, (68,214,144), 10)
pts = np.array([[10,50],[20,30],[70,20],[350,100]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (100,80,200), 2)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Sistemas Expertos',(10,250), font, 1, (200,255,155), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
