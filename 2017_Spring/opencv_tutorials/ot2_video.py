# ot2_video.py - read, display, and save video 

import cv2
import numpy as np

# load(a handle) video
cap = cv2.VideoCapture(0) # 0 is the first web cam 


# # 1. open a video frame
# while True:
# 	ret, frame = cap.read() # ret is true or false
# 	cv2.imshow('frame', frame)

# 	# display the video frame-by-frame for 1 ms
# 	# & close the frame when 'q' is entered
# 	if cv2.waitKey(1) & 0xFF == ord('q'): 
# 		break

# cap.release()
# cv2.destroyAllWindows()


# # 2. filter video into gray color
# while True:
# 	ret, frame = cap.read() # ret is true or false
# 	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 	cv2.imshow('frame', frame)
# 	cv2.imshow('gray', gray)

# 	# display the video frame-by-frame for 1 ms
# 	# & close the frame when 'q' is entered
# 	if cv2.waitKey(1) & 0xFF == ord('q'): 
# 		break

# cap.release()
# cv2.destroyAllWindows()


# 3. save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 2.0, (640, 480))

while True:
	ret, frame = cap.read() # ret is true or false
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out.write(frame)

	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)

	# display the video frame-by-frame for 1 ms
	# & close the frame when 'q' is entered
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

cap.release()
out.release()
cv2.destroyAllWindows()
