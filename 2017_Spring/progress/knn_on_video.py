# knn_on_video.py - load 3000 dataset and use them to train and test
import numpy as np
#import matplotlib.pyplot as plt
import cv2
import glob

file_names = glob.glob("data/*.png")
print("Loading " + str(len(file_names)) + " files.") 	# confirm the total number of file paths
file_names = np.sort(file_names)
#print(file_names[0:10]) # confirm first 11 file names

# read the first image
f = file_names[0]	
#print(f)
img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
images = np.array([img.flatten()]) # image is 250*200
#print(len(images))
#print(images[0].shape)
#print(images[0])

file_names = file_names[1:]
#print(len(file_names))

# save the image as an array = [200 elements for each 250 inside arrays] 
for f in file_names:
	img = cv2.imread(f, cv2.IMREAD_GRAYSCALE) # apply gray filter
	#print(img)
	images = np.append(images, [img.flatten()], axis=0)
	
#print(len(images)) 
print("total images: %d"%(len(images))) # should be 3000

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# make an array of labels
arr_1s = np.ones((1000,), dtype=np.int)
arr_2s = arr_1s + arr_1s
arr_3s = arr_2s + arr_1s

y = np.append(arr_1s, [arr_3s, arr_2s]) # y contains 1000 1s, 1000 3s, 1000 2s in this order

# split the dataset "images" and label "y"
x_train, x_test, y_train, y_test = train_test_split(images, y, test_size=0.2, random_state=42)
print("split training images: %d"%(len(x_train))) # should be 2400


num = 3 # number of neighbors for KNN

# Train
print("Training using KNN with %d neighbors."%(num))
neigh = KNeighborsClassifier(n_neighbors=num)
neigh.fit(x_train, y_train) 

# Test
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

