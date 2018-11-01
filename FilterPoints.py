from FilterPoints1 import FilterPoints1
from FilterPoints2 import FilterPoints2

def FilterPoints(points,framesize,linenum):
	fp1 = FilterPoints1(points,framesize,linenum)
	fp2 = FilterPoints2(points,framesize,linenum)
	return fp1 and fp2 

""" tested function: FilterPoints, test date: 15/5/17, status: OK 
logic test - test return value: 
print True and False
"""

""" test lists
framesize = [262,640]
p1  = [[142, 248], [582, 248]]
p2  = [[109, 247], [512, 247]]
p3  = [[178, 249], [582, 249]]
p4  = [[216, 250], [582, 250]]
p5  = [[220, 14], [381, 17]]
p6  = [[109, 228], [222, 15]]
p7  = [[459, 14], [489, 72]]
p8  = [[105, 241], [225, 15]]
p9  = [[107, 234], [223, 15]]
p10 = [[314, 13], [460, 18]]
p11 = [[105, 246], [371, 246]]
p12 = [[105, 245], [144, 171]]
p13 = [[386, 251], [581, 251]]
p14 = [[465, 14], [492, 67]]
p15 = [[461, 14], [491, 71]]
p16 = [[542, 169], [582, 247]]
p17 = [[222, 11], [346, 15]]
p18 = [[106, 245], [219, 245]]
p19 = [[464, 14], [491, 69]]
p20 = [[539, 169], [581, 247]]
p21 = [[350, 13], [459, 16]]
p22 = [[106, 244], [181, 244]]
p23 = [[190, 72], [220, 15]]
p24 = [[105, 239], [144, 166]]
p25 = [[378, 12], [429, 14]]
p26 = [[509, 252], [562, 252]]
"""









