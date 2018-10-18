import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys

img = cv2.imread('pullover_00.jpg')
img2 = cv2.imread('filename.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
rect = (0,0,900,900)
print(img.shape)



def grab(img, mask, rect):
  if(rect == None):
    constant = cv2.GC_INIT_WITH_MASK
  else:
    constant = cv2.GC_INIT_WITH_RECT
  bgdModel = np.zeros((1,65),np.float64)
  fgdModel = np.zeros((1,65),np.float64)
  cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,constant)
  mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
  img = img*mask2[:,:,np.newaxis]
  print("done")
  return img, mask2




img, mask = grab(img, mask,rect)
cv2.imshow("Figure 1", img)
cv2.waitKey(0)


while(True):
  print("give rectangle tuple")
  in_rect = [None]*4
  in_rect[0] = int(input())
  in_rect[1] = int(input())
  in_rect[2] = int(input())
  in_rect[3] = int(input())
  mask[in_rect[0]:(in_rect[0]+in_rect[2]), in_rect[1]:(in_rect[1]+in_rect[3])] = 0

  img, mask = grab(img, mask, None)
  cv2.imshow("Figure 1", img)

  cv2.waitKey(0)



