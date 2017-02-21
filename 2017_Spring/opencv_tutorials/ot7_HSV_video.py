# ot7_HSV_video.py - color filtering
# ref - https://en.wikipedia.org/wiki/HSL_and_HSV

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read() # undrscore for the return values that we don't care about

	# convert BTR to HSV(Hue Saturation Value)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	### ADJUST THE VALUE IN THE ARRAYS for HSV ###
	lower_col = np.array([20, 10, 50])
	upper_col = np.array([255, 255, 255])

		# # another method to convert BTR to HSV - not used here
		# dark_col = np.uint8([[[12, 22, 121]]])
		# dark_col = cv2.cvtColor(dark_col, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, lower_col, upper_col) # mask value will be 1 if in the range -> white
	res = cv2.bitwise_and(frame, frame, mask=mask ) # show color in frame where mask is 1

	# display all
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('result', res)


	k = cv2.waitKey(5) & 0xFF

	if k == 27: # 27 for ESC
		break

### common line ###
cv2.destroyAllWindows()
cap.release()


