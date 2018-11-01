def FilterPoints2(points,framesize,linenum):
	w1, h1, w2, h2 = points[0][0], points[0][1], points[1][0], points[1][1]
	height,width = framesize[0],framesize[1]
	if linenum == 1 or linenum == 2: # points in horizontal upper line
		if abs(h1 - h2)<5 and w1 < w2:
			return True
		else:
			return False
	if linenum == 3 : # points in left line
		if abs(h1 - h2)>10 and w1 < w2 and h1 > h2:
			return True
		else:
			return False
	if linenum == 4 : # points in right line
		if abs(h1 - h2)>10 and w1 < w2 and h1 < h2:
			return True
        else:
            return False

""" tested function: FilterPoints2, date: 15/5/17, status: OK 
print ""
framesize = [480, 640]

print ""
framesize = [480, 640]

points = [[11,13], [540, 15]] # w1<w2 and abs(h1-h2)<5
print FilterPoints2(points,framesize,linenum=1) # return True
print FilterPoints2(points,framesize,linenum=2) # return True

points = [[11,9], [540, 15]] # w1<w2 and abs(h1-h2)>5
print FilterPoints2(points,framesize,linenum=1) # return False
print FilterPoints2(points,framesize,linenum=2) # return False

points = [[540,13], [40, 15]] # w1>w2 and abs(h1-h2)<5
print FilterPoints2(points,framesize,linenum=1) # return False
print FilterPoints2(points,framesize,linenum=2) # return False

points = [[110,9], [40, 15]] # w1>w2 and abs(h1-h2)>5
print FilterPoints2(points,framesize,linenum=1) # return False
print FilterPoints2(points,framesize,linenum=2) # return False

framesize = [480, 640]
points = [[40,440], [110, 110]] #  abs(h1 - h2)>10 and w1 < w2 and h1 > h2:
print FilterPoints2(points,framesize,linenum=3) # return True
points = [[40,110], [110, 440]] #  abs(h1 - h2)>10 and w1 < w2 and h1 < h2:
print FilterPoints2(points,framesize,linenum=3) # return False
points = [[110,440], [40, 110]] #  abs(h1 - h2)>10 and w1 > w2 and h1 > h2:
print FilterPoints2(points,framesize,linenum=3) # return False
points = [[40,440], [110, 437]] #  abs(h1 - h2)<10 and w1 < w2 and h1 > h2:
print FilterPoints2(points,framesize,linenum=3) # return False
"""

