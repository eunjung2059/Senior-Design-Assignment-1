# ot16_faceDetection.py - object detection with Haar Cascades
# - need cascade files to do object recognition/detection
# - detect faces and eyes
# ref
# - https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/

import numpy as np
import cv2

# load cascade files
	# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect face on webcam input
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

        # in face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        # detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)

    cv2.imshow('img',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # ESC key
        break

cap.release()
cv2.destroyAllWindows()