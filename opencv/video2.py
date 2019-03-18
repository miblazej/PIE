# pylint: disable-msg=C0103
# pylint: disable-msg=C0111
import numpy as np
import cv2


CAP = cv2.VideoCapture('drop.avi')

while CAP.isOpened():
    ret, frame = CAP.read()

    GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', GRAY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
CAP.release()
cv2.destroyAllWindows()
