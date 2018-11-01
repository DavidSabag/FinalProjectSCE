def FilterPoints1(points,framesize,linenum):
    w1, h1, w2, h2 = points[0][0], points[0][1], points[1][0], points[1][1]
    height,width = framesize[0],framesize[1]
    if linenum == 1 : # points in horizontal upper line
        if h1 < 0.5*height and h2 < 0.5*height:
            return True
        else:
            return False
    if linenum == 2 : # points in horizontal lower line
        if h1 > 0.5*height and h2 > 0.5*height:
            return True
        else:
            return False
    if linenum == 3 : # points in left line
        if w1 < 0.5*width and w2 < 0.5*width:
               return True
        else:
            return False
    if linenum == 4 : # points in right line
        if w1 > 0.5*width and w2 > 0.5*width:
			return True
        else:
            return False

""" tested function: FilterPoints1, test date: 15/5/17, status: OK
print ""
framesize = [480, 640]

points = [[11,13], [540, 15]]
print FilterPoints1(points,framesize,linenum=1) # return True
points = [[11,400], [540, 410]]
print FilterPoints1(points,framesize,linenum=1) # return False

points = [[11,400], [540, 410]]
print FilterPoints1(points,framesize,linenum=2) # return True
points = [[11,13], [540, 15]]
print FilterPoints1(points,framesize,linenum=2) # return False

points = [[11,13], [12, 410]]
print FilterPoints1(points,framesize,linenum=3) # return True
points = [[400,13], [540, 400]]
print FilterPoints1(points,framesize,linenum=3) # return False

points = [[400,13], [540, 400]]
print FilterPoints1(points,framesize,linenum=4) # return True
points = [[11,13], [12, 410]]
print FilterPoints1(points,framesize,linenum=4) # return False
"""

