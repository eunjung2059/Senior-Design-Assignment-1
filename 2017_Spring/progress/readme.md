# Demo for final presentation. 

## 1. Get image dataset for ASL using `template files` and `getdata.py`.
	// related file: `getdata.py`
	// result(3000 images of ASL) is stored under `data` folder.
	- We make our own dataset from the web camera.
	- `getdata.py` produces about 1000 images of the target image(template image).
	- To do that, the file_name designating the template files should be changed for each template image.  
	
## 2. Load the dataset and use them to train and test.
	// related file: `load_data.py`
	// screen shot of the result is `knn_screenshot.png`.
	- Load the images into 2d arrays(`images`), and create 1d array label(`y`) 
	- Split the dataset(`images`) and label list(`y`) for training and testing. 
	- Try KNN whith several different number of neighbors(`num`). 
	- Decide the best `num`. // We think 3 is good enough
	
## 3. Apply the trained model to test the video input. 
	// related file: knn_on_video.py
	- Load the video from web camera
	- save `roi`(region of interest) into 2d array of one element
	- test the `roi` using the trained model and display on the video.  
	
