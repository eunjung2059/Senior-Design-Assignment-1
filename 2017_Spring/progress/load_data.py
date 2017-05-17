# load_data.py - load 3000 dataset and use them to train and test
import numpy as np
#import matplotlib.pyplot as plt
import cv2
import glob

file_names = glob.glob("data/*.png")
print(len(file_names)) 	# confirm the total number of file paths
file_names = np.sort(file_names)
print(file_names[0:10]) # confirm first 11 file names

# read the first image
f = file_names[0]	
#print(f)
img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
img_list = np.array([img]) # image is 250*200
#print(len(img_list))
#print(img_list)
file_names = file_names[1:]
#print(len(file_names))

# save the image as an array = [200 elements for each 250 inside arrays] 
for f in file_names:
	img = cv2.imread(f, cv2.IMREAD_GRAYSCALE) # apply gray filter
	#print(img)
	img_list = np.append(img_list, [img], axis=0)
	
print(len(img_list)) # on successful load, total should be 3000
