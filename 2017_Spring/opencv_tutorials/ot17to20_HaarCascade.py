# ot17to20_HaarCascade.py - create Haar Cascades for hand detection
# ref - https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

''' 
 Steps to make our own Haar Cascades
1. Collect thousands of "negative" or "background" images - target object is not included
		bg.txt file contains path to background images
			neg/1.jpg
			neg/2.jpg
			...
2. Collect or create "positive" images - target object
		pos.txt(info.txt) file contains path to negative images, num objects, start pt, rectangle coordinates
			pos/1.jpg 1 0 0 50 50  
			pos/2.jpg
			...
3. Create a positive vector file by stitching together all positives
4. Train cascade - with num_pos(50x50) = 2 * num_neg(100x100)
'''


### download-image-by-link.py ###
import urllib.request
import cv2
import numpy as np 
import os


### 1. Collect "negative" or "background" images
def store_raw_images():
    neg_images_link = '//image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")

            img = cv2.imread("neg/"+str(pic_num)+".jpg", cv2.IMREAD_GRAYSCALE)

            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))

            cv2.imwrite("neg/"+str(pic_num)+".jpg", resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e)) 
store_raw_images()

# delete ugly files
def find_uglies():
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)

                    # are they same images?
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)

                except Exception as e:
                    print(str(e))
find_uglies()

# write 'bg.txt' file
def create_pos_n_neg():
    for file_type in ['neg']: # can add 'pos' later
        
        for img in os.listdir(file_type):

            if file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt','a') as f:
                    f.write(line) 
            # elif file_type == 'pos':
            #     line = file_type + '/' + img + ' 1 0 0 50 50\n'
            #     with open('info.dat','a') as f:
            #         f.write(line)
create_pos_n_neg()

### 2. Create "positive" images from a sample
	# opencv tutorial 20 is about creanting samples using opencv_createsamples

### 3. Create a positive vector file
	# using opencv_createsamples again

### 4. Train cascade
	# using opencv_traincascade
