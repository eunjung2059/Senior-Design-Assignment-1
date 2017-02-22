# ot14_featureMatching.py - find template image that can be in different size, lighting, angle, or rotation
# ref 
# - https://pythonprogramming.net/feature-matching-homography-python-opencv-tutorial/
# - http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html

import numpy as np
import cv2
import matplotlib.pyplot as plt

# img1 = cv2.imread('opencv-feature-matching-template.jpg', 0)
# img2 = cv2.imread('opencv-feature-matching-image.jpg', 0)

# # feature detector
# orb = cv2.ORB_create()

# # find the key points and their descriptors
# kp1, des1 = orb.detectAndCompute(img1, None)
# kp2, des2 = orb.detectAndCompute(img2, None)

# # BFMatcher object
# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# matches = bf.match(des1,des2) # create matches of the descriptors
# matches = sorted(matches, key = lambda x:x.distance) # sort them based on their distances

# # draw the first 10 matches
# img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
# plt.imshow(img3)
# plt.show()


### with our data ###
#img1 = cv2.imread('ASL_one_captured.png', 0)
img1 = cv2.imread('ASL_one_rot.jpg', 0)
img2 = cv2.imread('ASL_one_youtube.png', 0)

# feature detector
orb = cv2.ORB_create()

# find the key points and their descriptors
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2) # create matches of the descriptors
matches = sorted(matches, key = lambda x:x.distance) # sort them based on their distances

# draw the first 10 matches
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
plt.imshow(img3)
plt.show()

cv2.imwrite('featureMatch.png', img3) 