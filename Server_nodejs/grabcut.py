import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('trouser_00.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
cv2.namedWindow('Figure 1',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Figure 1', 1000,1000)

rect = ()
print(type(rect))


def onMouse(event, x,y,flags, param):
  global rect   
  global img
  global mask 

  if(event == cv2.EVENT_LBUTTONDOWN):
    print(x,y)
    rect += (x,y)
    mask[x,y]=1
    #img = grab(img,mask,rect)
    img[x,y] = [255,255,255]
  elif(event == cv2.EVENT_LBUTTONUP):
    print(x,y)
    rect +=(x,y)
    print(type(rect))
    print(rect)
    img, mask = grab(img, mask,rect)
    cv2.imshow("Figure 1", img)
    cv2.waitKey(0)




def grab(img, mask, rect):
  bgdModel = np.zeros((1,65),np.float64)
  fgdModel = np.zeros((1,65),np.float64)
  cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
  mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
  img = img*mask2[:,:,np.newaxis]
  print("done")
  return img, mask2


cv2.setMouseCallback('Figure 1', onMouse, 0)



while(True):
  cv2.imshow("Figure 1", img)
  k = cv2.waitKey(500)
  if (k=='q'):
    break


