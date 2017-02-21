
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
import cv2


# In[2]:

# load a hand image
img = cv2.imread('hand.png', cv2.IMREAD_GRAYSCALE) # apply gray filter


# In[3]:

cv2.imshow('image', img)


# In[4]:

cv2.waitKey(0)


# In[5]:

cv2.destroyAllWindows()


# In[6]:

# display image using matplotlib.pyplot
plt.imshow(img, cmap='gray', interpolation='bicubic')


# In[7]:

plt.plot([50, 100], [80, 100], 'c', linewidth=5)


# In[8]:

plt.show()


# In[9]:

# save the gray filtered image
cv2.imwrite('grayhand.png', img)

