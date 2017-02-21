# ot9_transformation.py - morphological operations on shape to reduce nose
# ref  - https://pythonprogramming.net/morphological-transformation-python-opencv-tutorial/

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read() 

	# convert BTR to HSV(Hue Saturation Value)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	### ADJUST THE VALUE IN THE ARRAYS(HSV) for target image ###
	lower_col = np.array([20, 10, 50])
	upper_col = np.array([255, 255, 255])

	mask = cv2.inRange(hsv, lower_col, upper_col) # mask value will be 1 if in the range -> white
	res = cv2.bitwise_and(frame, frame, mask=mask ) # show color in frame where mask is 1
	# cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('result', res)

	### Erosion and Dilation ###
	kernel = np.ones((5,5), np.uint8)
	
	# 1. erosion 
	# - if all of the pixels are white, then we get white 
	erosion = cv2.erode(mask, kernel, iterations=1)
	# 2. dialation 
	# -  if the entire area isn't black, then it is converted to white 
	dilation = cv2.dilate(mask, kernel, iterations=1) # 
	cv2.imshow('erosion', erosion)
	cv2.imshow('dilation', dilation)

	### opening and closing ###
	# 3. opening removes false positives(white noise on the background)
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	# 4. closing removes false negatives(black noise on the target image)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	cv2.imshow('opening', opening)
	cv2.imshow('closing', closing)

### common line ###	
	k = cv2.waitKey(5) & 0xFF

	if k == 27: # 27 for ESC
		break

cv2.destroyAllWindows()
cap.release()

print("dilation works best to remove noise for hand")