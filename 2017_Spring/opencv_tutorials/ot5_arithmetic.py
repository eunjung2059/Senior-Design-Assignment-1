# ot5_arithmetic.py - arithmetic operations on images

import cv2
import numpy as np

# load same sized(500 x 250) images 
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')


### arithmetic operations ###

#1. add two images
add = img1+img2
cv2.imshow('img1+img2',add)
cv2.waitKey(0)

#2. "white" because color values above 255 is thresholded as 255 
add = cv2.add(img1, img2)
cv2.imshow('cv2.add',add)
cv2.waitKey(0)

#3. add with some transparency
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) # 0 is for gamma value(a measurement of light)
cv2.imshow('cv2.weighted',weighted)
cv2.waitKey(0)

### common line ###
cv2.destroyAllWindows()