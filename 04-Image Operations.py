import numpy as np
import cv2

img = cv2.imread(r'C:\Users\skinl\Pictures\carro.jpg',cv2.IMREAD_COLOR)

img[100:155,100:155] = [0,0,255]

copy_paste = img[37:111,107:194]
img[0:74,0:87] = copy_paste


cv2.imshow('imagen auto',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
