# ot4_image3.py - Image Operations

import cv2
import numpy as np

img = cv2.imread('hand.png', cv2.IMREAD_COLOR)


# #1. pixel value
# px = img[55,55] # color value of the pixel in [55, 55]
# print('color value in [55,55] is', px) 

# img[55,55] = [0,0,0] # change the color in that pixel into black
# print('color value in [55,55] is changed to', px) 


# #2. all the pixel values in the region of image
# roi = img[100:150, 100:150] 
# print(roi)
# img[100:150, 100:150] = [255, 0, 255] # change the color in roi

#3. region of thumb
thumb = img[180:250, 200:282] # thumb is arount that region
img[0:70, 0:82] = thumb # (0:250-180, 0:282-200)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()