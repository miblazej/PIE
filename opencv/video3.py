# pylint: disable-msg=C0103
# pylint: disable-msg=C0111
import numpy as np
import cv2

klatka = cv2.VideoCapture(0)

# Definicja kodeku oraz utworzenie obiektu Video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('zapis.avi', fourcc, 20.0, (640, 480))

while(klatka.isOpened()):
    ret, frame = klatka.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        # zapisanie klatki
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# zakonczenie wszystkiego gdy praca jest skonczona
klatka.release()
out.release()
cv2.destroyAllWindows()
