
# coding: utf-8

# In[1]:

import cv2
import numpy as np


# In[2]:

cap = cv2.VideoCapture(0) # 0 is the first web cam 


# In[ ]:

# opens a video frame
#while True:
#    ret, frame = cap.read() # ret is true or false
#    cv2.imshow('frame', frame)
    
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

#cap.release()
#cv2.destroyAllWindows()


# In[3]:

# save the video into files
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('first_record.avi', fourcc, 20.0, (640, 480)) # for 20 seconds, size is 640x480

# modify previous while loop to open two frames - one with gray
while True:
    ret, frame = cap.read() # ret is true or false
    
    # gray frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


# In[ ]:



