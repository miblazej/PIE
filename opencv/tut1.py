# Pylint Shut UP
import numpy as np
import cv2
from matplotlib import pyplot as plt

# wczytuje obraz
OBRAZ = cv2.imread('scrum.png', 0)
cv2.imshow('obraz', OBRAZ)
cv2.imwrite('scruma.png', OBRAZ)
plt.imshow(OBRAZ, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
