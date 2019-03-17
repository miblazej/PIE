# Pylint Shut UP
import numpy as np
import cv2

# wczytuje obraz
OBRAZ = cv2.imread('scrum.png', 0)
cv2.imshow('obraz', OBRAZ)
cv2.waitKey(0)
cv2.destroyAllWindows()


def dzialaczynie(brak):
    """Dzialanie poprawne

    Arguments:
        brak {brak} -- nazwa zmiennej majacej na celu wskazanie braku instenia zmiennej
    """
