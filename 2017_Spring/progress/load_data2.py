# load_data.py - load 3000 dataset and use them to train and test
import numpy as np
#import matplotlib.pyplot as plt
import cv2
import glob
from skimage import io


file_names = glob.glob("data/*.png")
print(len(file_names)) 	# confirm the total number of file paths
file_names = np.sort(file_names)
print(file_names[0:10]) # confirm first 11 file names


images = io.imread_collection(file_names)
print(images[0])
