# getdata.py - save 1000 dataset to under the data folder
import cv2
import numpy as np
import io

############################ filename ######################################
tmpl = cv2.imread('template2/one.png',0) # 0 to Loads image in grayscale mode


# load(a handle) video
cap = cv2.VideoCapture(0) # 0 is the first web cam 

#set the width and height of the capture
#cap.set(3,200) # CV_PROP_FRAME_WIDTH
#cap.set(4,250) # CV_PROP_FRAME_HEIGHT

i = 1
while (True and (i <= 1000)):
	ret, frame = cap.read() # ret is true or false

	# 1. draw a rectangle ROI - Region Of Interest is (50, 200), (250, 450)
	cv2.rectangle(frame, (50, 200), (250, 450), (0, 255, 0), 3)
	roi = frame[200:450, 50:250] # [y points, x points]

	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	#cv2.imwrite('roi.png', roi)
	
	# 2. write some text
	font = cv2.FONT_HERSHEY_SIMPLEX
	# putText(where, what, loc, style, size, BGR, thickness, lineType)
	cv2.putText(frame, '"Enter q to quit."', (10, 50), font, 1, (0, 255, 0), 1, cv2.LINE_AA) 
	
	### 3. template match ###
	res1 = cv2.matchTemplate(gray, tmpl, cv2.TM_CCOEFF_NORMED)
	
	# find by adjusting the threshold value
	threshold = 0.66

	#loc1 = np.where(res1 >= threshold)
	#print(loc1)
	#for pt in zip(*loc1[::-1]):
	#------------------------------------------------------------------------
	if np.sum(res1 >= threshold) > 100:
##################################### filename_ #########################
		cv2.imwrite("data/" + "one_" + str(i) + ".png", roi)
		#cv2.imwrite("data/" + "nth_" + str(i) + ".png", roi)
		print("saved " + str(i))
		i = i + 1
	#------------------------------------------------------------------------

	#out.write(frame)
	mirror = cv2.flip(frame,1)
	cv2.imshow('mirror view', mirror)

	# display the video frame-by-frame for 1 ms
	# & close the frame when 'q' is entered
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

cap.release()
cv2.destroyAllWindows()






