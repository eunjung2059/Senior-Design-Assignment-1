# ot10_edge_gradients.py - Edge Detection and Gradients
# ref - https://pythonprogramming.net/canny-edge-detection-gradients-python-opencv-tutorial/?completed=/morphological-transformation-python-opencv-tutorial/

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	# Take each frame
	_, frame = cap.read()
	# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# lower_red = np.array([30,150,50])
	# upper_red = np.array([255,255,180])

	# mask = cv2.inRange(hsv, lower_red, upper_red)
	# res = cv2.bitwise_and(frame,frame, mask= mask)

	# laplacian filter
	laplacian = cv2.Laplacian(frame, cv2.CV_64F) # like bad signaled old TV
	cv2.imshow('laplacian',laplacian)

	### gradiants ###
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
	cv2.imshow('sobelx',sobelx)
	cv2.imshow('sobely',sobely)

	### edge detection ###
	edges = cv2.Canny(frame, 100, 100) # increase numbers to reduce noise
	cv2.imshow('edges', edges)

	# cv2.imshow('Original',frame)
	# cv2.imshow('Mask',mask)
	
### common line ###	
	k = cv2.waitKey(5) & 0xFF

	if k == 27: # 27 for ESC
		break

cv2.destroyAllWindows()
cap.release()

print("dilation works best to remove noise for hand")