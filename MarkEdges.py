import cv2
import numpy as np

def MarkEdges(frame):
	grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # convert frame to rgb 
	bwframe	= cv2.Canny(grayframe, 100, 250, apertureSize = 3) # mark edges 
	kernel = np.ones((5,5),np.uint8) # creates a kernel for the lest fnction
	return cv2.dilate(bwframe, kernel, iterations = 1) # remark edges 

""" teted function: MarkEdges, test date: 15/5/17, status: OK
frame = cv2.imread('Img28C.jpg')
res = MarkEdges(frame)
cv2.imshow('frame',frame)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""





