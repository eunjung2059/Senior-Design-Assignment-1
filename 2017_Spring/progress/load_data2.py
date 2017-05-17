# load_data2.py - load 3000 dataset and use them to train and test
import numpy as np
#import matplotlib.pyplot as plt
import cv2
import glob
from skimage import io
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

file_names = glob.glob("data/*.png")
# print(len(file_names)) 	# confirm the total number of file paths
file_names = np.sort(file_names)
# print(file_names[0:10]) # confirm first 11 file names


images = io.imread_collection(file_names)
#print(images.files[0]) # should be 'data/one_1.png'
#print(images.files[1000]) # should be 'data/three_1.png'
#print(images.files[2000]) # should be 'data/two_1.png'
#print(images[0].shape)

arr_1s = np.ones((1000,), dtype=np.int)
arr_2s = arr_1s + arr_1s
arr_3s = arr_2s + arr_1s

y = np.append(arr_1s, [arr_3s, arr_2s]) # y contains 1000 1s, 1000 3s, 1000 2s in this order

# split the dataset "images" and label "y"
x_train, x_test, y_train, y_test = train_test_split(images, y, test_size=0.2, random_state=42)


#neigh = KNeighborsClassifier(n_neighbors=3)
#neigh.fit(x_train, y_train) 
#guesses = neigh.predict(x_test)
#pred_prob = neigh.predict_proba(x_test)
#print(guesses)
#print(pred_prob)
knn = cv2.ml.KNearest_create()
#knn.train(x_train,y_train)
knn.train(x_train,cv2.ml.ROW_SAMPLE,y_train)
ret, results, neighbours ,dist = knn.find_nearest(y_test, 3)

print "result: ", results,"\n"
print "neighbours: ", neighbours,"\n"
print "distance: ", dist
