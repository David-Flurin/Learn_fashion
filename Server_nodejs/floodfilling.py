import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('filename.jpg')
plt.imshow(img),plt.show()

h, w = img.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
seed = (100,100)
img_flood = img.copy()

cv2.floodFill(img_flood, mask, seed, 0)
#img = img*mask[:,:,np.newaxis]

img_flood_inv = cv2.bitwise_not(img_flood)

# Combine the two images to get the foreground.
im_out = img | img_flood_inv

plt.imshow(im_out),plt.colorbar(),plt.show()