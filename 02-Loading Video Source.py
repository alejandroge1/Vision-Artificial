import numpy as np
import cv2

captura = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    ret, frame = captura.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('video--ventana1',frame)
    cv2.imshow('video--ventana2',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
out.release()
cv2.destroyAllWindows()
