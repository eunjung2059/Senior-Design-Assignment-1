# ot6_threshold.py - threshold on images
# ref - https://pythonprogramming.net/thresholding-image-analysis-python-opencv-tutorial/
# ref - http://docs.opencv.org/3.2.0/d7/d4d/tutorial_py_thresholding.html

import cv2
import numpy as np

# original image of the bookpage
img = cv2.imread('bookpage.jpg')
cv2.imshow('original',img)
cv2.waitKey(0)

# threshold on color image
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)

# threshold on gray image
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2gray = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold2gray',threshold2gray)
cv2.waitKey(0)

# adaptive threshold - 255 is the max value
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('cv2.adaptiveThreshold',gaus)
cv2.waitKey(0)

# Otsu's threshold
retval3,otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu threshold',otsu)
cv2.waitKey(0)

### common line ###
cv2.destroyAllWindows()