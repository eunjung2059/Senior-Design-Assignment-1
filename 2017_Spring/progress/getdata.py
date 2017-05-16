# getdata.py - save 1000 dataset to under the data folder
import cv2
import numpy as np
import io

# load(a handle) video
cap = cv2.VideoCapture(0) # 0 is the first web cam 

i = 1
while (True or (i >= 1000)):
	ret, frame = cap.read() # ret is true or false
	
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# 1. draw a rectangle ROI - Region Of Interest is (50, 200), (250, 450)
	cv2.rectangle(frame, (50, 200), (250, 450), (0, 255, 0), 3)
	roi = frame[200:450, 50:250] # [y points, x points]
	
	#cv2.imwrite('roi.png', roi)
	#------------------------------------------------------------------------
	cv2.imwrite("data/one_" + str(i) + ".png", roi)
	i = i + 1
	#------------------------------------------------------------------------

	# 2. write some text
	font = cv2.FONT_HERSHEY_SIMPLEX
	# putText(where, what, loc, style, size, BGR, thickness, lineType)
	cv2.putText(frame, '"Enter q to quit."', (10, 50), font, 1, (0, 255, 0), 1, cv2.LINE_AA) 

	cv2.imshow('frame', frame)

	# display the video frame-by-frame for 1 ms
	# & close the frame when 'q' is entered
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

cap.release()
cv2.destroyAllWindows()






