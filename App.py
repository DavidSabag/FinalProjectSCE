import cv2
from MarkEdges import MarkEdges
from GetListsOfPoints import GetListsOfPoints
from PointsFromLines import PointsFromLines
from FrameTransform import FrameTransform
from CropFrame import CropFrame
from CheckList import CheckList
from CheckPoints import CheckPoints
from AvgPoints import AvgPoints
from PointsDistence import PointsDistence

def App(cam = 0):
    Path = '/home/avizaudi/FP/FPBaseCode/00-Files4Testing/VIdeos/Vid4.avi' # TEST
    cap = cv2.VideoCapture(Path) # TEST
    #SILENCE cap = cv2.VideoCapture(cam)
    listofpoints = [[],[],[],[]]
    avgpoints = None
    #SILENCE outputimage = None
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            cropframe = CropFrame(frame)
            markedframe = MarkEdges(cropframe)
            listofpoints = GetListsOfPoints(markedframe,listofpoints)
            if CheckList(listofpoints):
                points = PointsFromLines(listofpoints)
                if CheckPoints(cropframe, points):
                    if avgpoints == None:
                        avgpoints = list(points)
                    else:
                        if PointsDistence(avgpoints, points, 5):
                            avgpoints = AvgPoints(avgpoints, points)
                            subframe = FrameTransform(cropframe,avgpoints)
                            markedframe = FrameTransform(markedframe,avgpoints)
                            cv2.imshow('subframe',subframe) # TEST
                            cv2.imshow('markedframe',markedframe) # TEST
                            #SILENCE outputimage = Step4(subframe)
                listofpoints = [[],[],[],[]]
        if cv2.waitKey(1) & 0xFF == ord('q'):
			break

    #end - save image
    
    cap.release()    
    cv2.destroyAllWindows()
    
    
App()
