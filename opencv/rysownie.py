# pylint: disable-msg=C0103
# pylint: disable-msg=C0111

import numpy as np
import cv2

# stworz czarny obraz
obraz = np.zeros((512, 512, 3), np.uint8)

# Narysuja diagonalna niebieska linie o grubosci 5 pixeli
obraz = cv2.line(obraz, (0, 0), (511, 511), (255, 0, 0), 5)
# Narysuj prostokąt
obraz = cv2.rectangle(obraz, (384, 0), (510, 128), (0, 255, 0), 3)
# Narysuje kolka
obraz = cv2.circle(obraz, (447, 63), 63, (0, 0, 255), -1)
# Narysuj eklipse
obraz = cv2.ellipse(obraz, (255, 256), (100, 50), 0, 0, 180, 255, -1)
# Wielokat najpierw musisz miec szereg z wiercholkami
punkty = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
punkty = punkty.reshape((-1, 1, 2))
obraz = cv2.polylines(obraz, [punkty], True, (0, 255, 255))
# Dodawania tekstu do obrazu
czcionka = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(obraz, 'OPENCV TEST', (10, 500), czcionka,
            4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('obraz', obraz)
cv2.waitKey(0)
cv2.destroyAllWindows()
