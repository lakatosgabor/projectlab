import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow


def getCircle():
  img = cv.imread('t.jpg',0)
  img = cv.medianBlur(img,5)
  cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
  circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1, 60,
                              param1=50,param2=80,minRadius=0,maxRadius=0)
  circles = np.uint16(np.around(circles))

  count = 0;
  for i in circles[0,:]:
      count+=1
      # draw the outer circle
      cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
      # draw the center of the circle
      cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
  cv2_imshow(cimg)
  cv.waitKey(0)
  cv.destroyAllWindows()

  print("\nCircle number: {}".format(len(circles[0,:])))
