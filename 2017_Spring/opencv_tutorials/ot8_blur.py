# ot8_blur.py - get rid of nose
# ref  - http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read() # undrscore for the return values that we don't care about

	# convert BTR to HSV(Hue Saturation Value)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	### ADJUST THE VALUE IN THE ARRAYS(HSV) for target image ###
	lower_col = np.array([20, 10, 50])
	upper_col = np.array([255, 255, 255])

		# # another method to convert BTR to HSV - not used here
		# dark_col = np.uint8([[[12, 22, 121]]])
		# dark_col = cv2.cvtColor(dark_col, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, lower_col, upper_col) # mask value will be 1 if in the range -> white
	res = cv2.bitwise_and(frame, frame, mask=mask ) # show color in frame where mask is 1

	# display all
	# cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('result', res)

	### SMOOTH ###
		# kernel can be either low-pass filters(LPF) or high-pass filters(HPF)
		# LPF helps in removing noises, blurring the images etc. 
		# HPF filters helps in finding edges in the images.
	kernel = np.ones((15,15), np.float32)/225  # 15x15 pixel each value of 1/(15*15)
	smoothed = cv2.filter2D(res, -1, kernel)
	cv2.imshow('smoothed', smoothed)

	### BLUR ###
	blur = cv2.GaussianBlur(res, (15, 15), 0) 
		# width and height of kernel should be odd
		# effective in removing gaussian noise 
	cv2.imshow('blur', blur)

	median = cv2.medianBlur(res, 15)
	cv2.imshow('median', median)

	bilateral = cv2.bilateralFilter(res, 15, 75, 75)
	cv2.imshow('bilateral', bilateral)

### common line ###	
	k = cv2.waitKey(5) & 0xFF

	if k == 27: # 27 for ESC
		break

cv2.destroyAllWindows()
cap.release()

print("Looks like MEDIAN is the best filter for hand seperation")