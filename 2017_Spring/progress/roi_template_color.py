# roi_template.py - set roi then use template matching on roi for object recognition

import cv2
import numpy as np

# load(a handle) video
cap = cv2.VideoCapture(0) # 0 is the first web cam 

# read template images
tmpl_one = cv2.imread('templates/one.png')#,0) # 0 to Loads image in grayscale mode

# save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480)) #([filename, fourcc, fps, frameSize[, isColor]]) 

i = 1
while True:
	ret, frame = cap.read() # ret is true or false
	
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# 1. draw a rectangle ROI - Region Of Interest is (50, 200), (250, 450)
	cv2.rectangle(frame, (50, 200), (250, 450), (0, 255, 0), 3)
	roi = frame[200:450, 50:250] # [y points, x points]
	cv2.imwrite('roi.png', roi)
	# target region to search
	#roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

	# 2. write some text
	font = cv2.FONT_HERSHEY_SIMPLEX
	# putText(where, what, loc, style, size, BGR, thickness, lineType)
	cv2.putText(frame, '"Enter q to quit."', (10, 50), font, 1, (0, 255, 0), 1, cv2.LINE_AA) 

	### 3. template match ###
	res1 = cv2.matchTemplate(roi, tmpl_one, cv2.TM_CCOEFF_NORMED)
	
	# find by adjusting the threshold value
	threshold = 0.66
	loc1 = np.where(res1 >= threshold)
	print(loc1)
	for pt in zip(*loc1[::-1]):
		cv2.putText(frame, '"One"', (30, 100), font, 1, (0, 255, 255), 3, cv2.LINE_AA) 	
		cv2.imwrite('detected_1.png', roi)

	out.write(frame)

	cv2.imshow('frame', frame)
	#cv2.imshow('gray', gray)

	# display the video frame-by-frame for 1 ms
	# & close the frame when 'q' is entered
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

cap.release()
out.release()
cv2.destroyAllWindows()






