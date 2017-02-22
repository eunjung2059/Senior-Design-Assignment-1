# ot15_reduce_bgr.py - reduce the background of images by detecting motion
# - https://pythonprogramming.net/mog-background-reduction-python-opencv-tutorial/
# - http://docs.opencv.org/3.0-beta/modules/video/doc/motion_analysis_and_object_tracking.html#createbackgroundsubtractormog

import numpy as np
import cv2

# cap = cv2.VideoCapture('people-walking.mp4')
cap = cv2.VideoCapture('ASL_numbers.mp4')
# cap = cv2.VideoCapture(0) # for the webcam

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
 
    cv2.imshow('original', frame)
    cv2.imshow('fgmask', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # ESC key
        break
    
cap.release()
cv2.destroyAllWindows()