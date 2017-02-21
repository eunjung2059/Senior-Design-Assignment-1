# ot1_image.py - read, display, and save image 

import numpy as np
import matplotlib.pyplot as plt
import cv2


# 1. load a hand image
img = cv2.imread('hand.png', cv2.IMREAD_GRAYSCALE) # apply gray filter
	# other flags for imread()
	# 	IMREAD_COLOR		OR 1
	# 	IMREAD_UNCHANGED	OR -1

# # display image
# cv2.imshow('image', img)
# cv2.waitKey(0) 
	# wait for any key to be pressed infinitely
	# waitKey(25) will display a frame for 25 ms, after which display will be automatically closed.
# cv2.destroyAllWindows()


# 2. display image using matplotlib.pyplot
plt.imshow(img, cmap='gray', interpolation='bicubic')
	# watch out when using color :
	# - opencv uses BGR while matplotlib uses RGB

# draw a line (x_points, y_points, cyan_color)
plt.plot([50, 100], [80, 100], 'c', linewidth=5)
plt.show()

# save the gray filtered image
cv2.imwrite('grayhand.png', img)
