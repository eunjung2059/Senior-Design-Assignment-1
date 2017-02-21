# ot3_image2.py - Drawing and Writing on Image
# refer - http://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html

import cv2
import numpy as np

img = cv2.imread('hand.png', cv2.IMREAD_COLOR) # read an image in color


# 1. draw a line
cv2.line(img, (0,0), (150,150), (255, 0, 0), 15) # (where, start_pt, end_pt, BGR, width)

# 2. draw a rectangle
cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)

# 3. draw a circle
cv2.circle(img, (100, 63), 55, (0, 0, 255), -1) # (where, center, radius, BGR, -1 to fillin)

# 4. draw a polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50,10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255), 3) # True to connect the final point to the first one


# 5. write some text
font = cv2.FONT_HERSHEY_SIMPLEX
# putText(where, what, loc, style, size, BGR, thickness, lineType)
cv2.putText(img, 'OpenCV Tuts!', (0, 130), font, 1, (0, 0, 0), 3, cv2.LINE_AA) 

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
