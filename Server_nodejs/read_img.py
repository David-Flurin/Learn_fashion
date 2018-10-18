import numpy as np 
import cv2
from pandas import HDFStore,DataFrame

def downscale(img,res):
	dims =img.shape
	size = min(dims)
	highest_res = 2
	while(highest_res<size):
		highest_res *= 2
	highest_res /= 2
	img = cv2.resize(img, (0,0), fx=highest_res/dims[1], fy= highest_res/dims[0])
	while(highest_res >= res*2):
		img = cv2.resize(img, (0,0), fx=0.5, fy= 0.5) 
		highest_res /= 2
	if highest_res != res:
		img = cv2.resize(img, (0,0), fx=res/highest_res, fy= res/highest_res)
	return img


def load_image(path, res):
	img = np.array(cv2.imread(path,cv2.IMREAD_GRAYSCALE))
	dims = img.shape
	return downscale(img,res)


def load_images(low_border_j, low_border_i,border_j,border_i):
	print(str(border_i) + " "+str(border_j))
	images = []
	file = open("testfile.txt","w")
	for j in range(low_border_j,border_j+1):
		for i in range(low_border_i,border_i+1):
			string_I = '0'+str(i) if i < 10 else str(i)
			string_J = '0'+str(j) if j < 10 else str(j)
			path = 'English/Hnd/Img/Sample0' + string_J +'/img0' + string_J + '-0'+string_I+'.png'
			images.append(np.insert(load_image(path,128.), 0,j-1, axis=0))
	return images








