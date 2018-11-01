import numpy as np
import cv2
from FixPoints import FixPoints

def FrameTransform(frame,points):
    frameheight,framewidth = frame.shape[0],frame.shape[1]
    points = FixPoints(points, fix=5)

    W = int((0.4)*framewidth) # points[1][0] - points[0][0]
    H = int(W*1.2)
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[W,0],[0,H],[W,H]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(frame,M,(W,H))
    
    height,width = dst.shape[0],dst.shape[1]
    M = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
    return cv2.warpAffine(dst, M, (width, height))

""" tested function: FrameTransform, test date: 16/5/17, status: OK 
frame = cv2.imread('Img28C.jpg')

points = [[223,12],[462,15],[102,246],[582,250]]
subframe = FrameTransform(frame,points)
cv2.imshow('subframe',subframe)

k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()
"""

