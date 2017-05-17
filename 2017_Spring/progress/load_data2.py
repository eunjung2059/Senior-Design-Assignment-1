# load_data2.py - load 3000 dataset and use them to train and test
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
print(images.files[0]) # should be 'data/one_1.png'
print(images.files[1000]) # should be 'data/three_1.png'
print(images.files[2000]) # should be 'data/two_1.png'

arr_1s = np.ones((1000,), dtype=np.int)
arr_2s = arr_1s + arr_1s
arr_3s = arr_2s + arr_1s

y = np.append(arr_1s, [arr_2s, arr_3s]) # y contains 1000 1s, 1000 2s, 1000 3s in this order  
