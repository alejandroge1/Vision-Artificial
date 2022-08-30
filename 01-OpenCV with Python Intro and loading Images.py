import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\skinl\Pictures\carro.jpg" ,cv2.IMREAD_GRAYSCALE)

cv2.imshow('ventana imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,250],[100,200],'r', linewidth=5)
plt.show()
'''

#cv2.imwrite(r'C:\Users\skinl\Pictures\carro2.jpg',img)

