# ot12_foreground.py - find foreground(remove background) manually
# ref 
# - https://pythonprogramming.net/grabcut-foreground-extraction-python-opencv-tutorial/
# - http://docs.opencv.org/3.2.0/d8/d83/tutorial_py_grabcut.html

import cv2
import numpy as np 
import matplotlib.pyplot as plt

# img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')
# mask = np.zeros(img.shape[:2],np.uint8)

# bgdModel = np.zeros((1,65),np.float64)
# fgdModel = np.zeros((1,65),np.float64)

# # rect = (161, 79, 150, 150) # rectangle around head
# rect = (50, 50, 300, 500) # rectangle around body

# # remove background around rect
# cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
# mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
# img = img*mask2[:, :, np.newaxis]
# plt.imshow(img)
# plt.colorbar()
# plt.show()

### with our data ###
img = cv2.imread('ASL_one_youtube.png')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

# foreground object in the format (x,y,w,h)
rect = (365, 160, 85, 170) # rectangle around hand on the right side

# remove background around rect
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
img = img*mask2[:, :, np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()

cv2.imwrite('forground.png', img)