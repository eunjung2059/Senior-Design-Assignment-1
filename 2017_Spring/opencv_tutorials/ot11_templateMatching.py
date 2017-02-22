# ot11_templateMatching.py - template matching for object recognition
# ref 
# - https://pythonprogramming.net/template-matching-python-opencv-tutorial/
# - http://docs.opencv.org/3.2.0/d4/dc6/tutorial_py_template_matching.html

import cv2
import numpy as np

### 1. using the data on tutorial ###
# img_bgr = cv2.imread('opencv-template-matching-python-tutorial.jpg')
# img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# template = cv2.imread('opencv-template-for-matching.jpg',0)
# w, h = template.shape[::-1]
# 	# needs -1 since template is 19x22 pixels, but template.shape[::] returns them in the reversed order

# res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# threshold = 0.8
# loc = np.where(res >= threshold)

# for pt in zip(*loc[::-1]):
# 	cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

# cv2.imwrite('detected.png', img_bgr)
# cv2.imshow('detected', img_bgr)
# cv2.waitKey(0)
# cv2.distroyAllWindows()


### 2. with our data ###
img_bgr = cv2.imread('ASL_one_youtube.png')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('ASL_one_captured.png',0)
w, h = template.shape[::-1]
	# needs -1 since template is 19x22 pixels, but template.shape[::] returns them in the reversed order

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# 1. find with high threshold
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1)
cv2.imwrite('detected_1.png', img_bgr)

cv2.imshow('detect with high threshold', img_bgr)
cv2.waitKey(0)

# 2. find with low threshold
threshold = 0.6
loc = np.where(res >= threshold)

img_bgr = cv2.imread('ASL_one_youtube.png') # read again to undo # 1

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1)
cv2.imwrite('detected_2.png', img_bgr)
cv2.imshow('detect with low threshold', img_bgr)
cv2.waitKey(0)

cv2.distroyAllWindows()
