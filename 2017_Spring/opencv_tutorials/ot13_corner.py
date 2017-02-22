# ot13_corner.py - corner detection 
#	to track motion 
#	to do 3D modeling, 
#	to recognize objects, shapes, and characters.
# ref 
# - https://pythonprogramming.net/corner-detection-python-opencv-tutorial/
# - http://docs.opencv.org/3.0-beta/modules/imgproc/doc/feature_detection.html#goodfeaturestotrack

import cv2
import numpy as np

# ### with data on tutorial ###
# img = cv2.imread('opencv-corner-detection-sample.jpg')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)

# # goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance)
# corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# corners = np.int0(corners)

# for corner in corners:
# 	x,y = corner.ravel()
# 	cv2.circle(img, (x,y), 3, 255, -1)
    
# cv2.imshow('Corner', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



### with our data ###
img = cv2.imread('ASL_one_youtube.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150) # cv2.Canny(image, threshold1, threshold2)
# cv2.imshow('edges', edges)
edges = np.float32(edges)

# goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance)
corners = cv2.goodFeaturesToTrack(edges, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
	x,y = corner.ravel()
	cv2.circle(img, (x,y), 3, 255, -1)
    
cv2.imshow('Corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
