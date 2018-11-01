import cv2
import numpy as np
from FilterPoints import FilterPoints
from AddToList import AddToList

def GetListsOfPoints(markedframe,listofpoints):
	lines = cv2.HoughLinesP(markedframe,1,np.pi/180,20,2000,50)[0]
	for w1,h1,w2,h2 in lines:
		points = [[w1,h1], [w2,h2]]
		framesize = [markedframe.shape[0], markedframe.shape[1]]
		if FilterPoints(points,framesize,linenum=1):
			listofpoints = AddToList(listofpoints, points, linenum=1)
		if FilterPoints(points,framesize,linenum=2):
			listofpoints = AddToList(listofpoints, points, linenum=2)
		if FilterPoints(points,framesize,linenum=3):
			listofpoints = AddToList(listofpoints, points, linenum=3)
		if FilterPoints(points,framesize,linenum=4):
			listofpoints = AddToList(listofpoints, points, linenum=4)
	return listofpoints
    
