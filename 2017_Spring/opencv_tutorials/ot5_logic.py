# ot5_logic.py - logic operations on images

import cv2
import numpy as np

# load same sized(500 x 250) images 
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

### logical operations ###

#1. img2
cv2.imshow('img2',img2)
cv2.waitKey(0)

# find out the size of img2
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

#2. convert the image into gray
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('img2gray',img2gray)
cv2.waitKey(0)

#3. threshold 220 
# - pixelvalue above 220 is converted to 255, otherwise to 0
# ref - http://docs.opencv.org/3.2.0/d7/d4d/tutorial_py_thresholding.html
ret, thresholded = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)
cv2.imshow('thresholded',thresholded)
cv2.waitKey(0)

#4. mask : inverse the threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('mask',mask)
cv2.waitKey(0)

#5. mask inversed : same with thresholded
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv', mask_inv)
cv2.waitKey(0) 

#6. mask img1 with mask_inv
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv) 
cv2.imshow('img1_bg', img1_bg)
cv2.waitKey(0)

#7. mask img2 with mask
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
cv2.imshow('img2_fg', img2_fg)
cv2.waitKey(0)

#8. img1_bg + img2_fg
dst = cv2.add(img1_bg, img2_fg)
cv2.imshow('dst', dst)
cv2.waitKey(0)

#9. copy and paste dst into img1
img1[0:rows, 0:cols] = dst
cv2.imshow('result', img1)
cv2.waitKey(0)

### common line ###
cv2.destroyAllWindows()