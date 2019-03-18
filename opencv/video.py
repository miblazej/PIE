import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    """Petla przechwytujaca poszczegolne klatki
    """
    # zlapanie klatki po klatce
    ret, frame = cap.read()
    # operacja na klatce
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # wyswietlenie klatki w resultacie
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.realease()
cv2.destroyAllWindows()
