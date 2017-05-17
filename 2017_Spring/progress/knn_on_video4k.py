# knn_on_video.py - load 3000 dataset and use them to train and test
import numpy as np
#import matplotlib.pyplot as plt
import cv2
import glob

## 1. save all the file paths under "data/" directory into an array "file_names"
file_names = glob.glob("data/*.png")
print("Loading " + str(len(file_names)) + " files.") 	# confirm the total number of file paths
file_names = np.sort(file_names)
#print(file_names[0:10]) # confirm first 11 file names
# should be 4000 images

## 2. read the first image
f = file_names[0]	
#print(f)
img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
images = np.array([img.flatten()]) # image is 250*200 = 50000
#print(len(images))
#print(images[0].shape)
#print(images[0])

file_names = file_names[1:]
#print(len(file_names))

## 3. save the rest image as an array = [an array of 50000 elements for each image] 
for f in file_names:
	img = cv2.imread(f, cv2.IMREAD_GRAYSCALE) # apply gray filter
	#print(img)
	images = np.append(images, [img.flatten()], axis=0)
	
#print(len(images)) 
print("total images: %d"%(len(images))) # should be 4000

## 4. Apply KNN
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# make an array of labels
arr_nth = np.zeros((1000,), dtype=np.int)
arr_1s = np.ones((1000,), dtype=np.int)
arr_2s = arr_1s + arr_1s
arr_3s = arr_2s + arr_1s

# y contains 1000 0s for nth, 1000 1s, 1000 3s, 1000 2s in this order
y = np.append(arr_nth, [arr_1s, arr_3s, arr_2s]) 

# split the dataset "images" and label "y"
x_train, x_test, y_train, y_test = train_test_split(images, y, test_size=0.2, random_state=42)
print("split training images: %d"%(len(x_train))) # should be 3200


num = 3 # number of neighbors for KNN

## 4-1. Train
print("Training using KNN with %d neighbors."%(num))
neigh = KNeighborsClassifier(n_neighbors=num)
neigh.fit(x_train, y_train) 

## 4-2. Test
print("Testing.")
guesses = neigh.predict(x_test)
#pred_prob = neigh.predict_proba(x_test)
#print(guesses)
#print(y_test)
#print(pred_prob)

# calculate correctness in percetage
correct = np.sum(np.equal(y_test, guesses))
print("Among %d testing %d were correct."%(len(y_test), correct))

correct_percent = correct/(len(y_test))*100.0
print(correct_percent)
print("Correct %7.2f on test set."%(correct_percent))

## 5. Test on the image from the captured video.

# load(a handle) video
cap = cv2.VideoCapture(0) # 0 is the first web cam 

i = 1
while True:
	ret, frame = cap.read() # ret is true or false
	
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	## 5-1. draw a rectangle ROI - Region Of Interest is (50, 200), (250, 450)
	cv2.rectangle(frame, (50, 200), (250, 450), (0, 255, 0), 3)
	roi = frame[200:450, 50:250] # [y points, x points]
	
	# target region to test
	roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	v_test = np.array([roi_gray.flatten()]) # v_test is a 2d array of  one element
	#print(v_test.shape) # should be (1, 50000)

	### 5-2. Test with the video ###
	#res1 = cv2.matchTemplate(roi_gray, tmpl_one, cv2.TM_CCOEFF_NORMED)
	res = neigh.predict(v_test)
	print(res)
	
	## 5-3. write some text
	font = cv2.FONT_HERSHEY_SIMPLEX
	# putText(where, what, loc, style, size, BGR, thickness, lineType)
	if res in np.array([1,2,3]):
		cv2.putText(frame, str(res), (10, 50), font, 1, (255, 0, 0), 3, cv2.LINE_AA) 
	else:
		cv2.putText(frame, '"Enter q to quit."', (10, 50), font, 1, (0, 255, 0), 1, cv2.LINE_AA) 

	# find by adjusting the threshold value
	#threshold = 0.66
	#loc1 = np.where(res1 >= threshold)
	#print(loc1)
	#for pt in zip(*loc1[::-1]):
	#	cv2.putText(frame, '"One"', (30, 100), font, 1, (0, 255, 255), 3, cv2.LINE_AA) 	
	#	cv2.imwrite('detected_1.png', roi)
	
	# display on the video
	mirror = cv2.flip(frame, 1)
	cv2.imshow('mirror view', mirror)


	# display the video frame-by-frame for 1 ms
	# & close the frame when 'q' is entered
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

cap.release()
cv2.destroyAllWindows()


