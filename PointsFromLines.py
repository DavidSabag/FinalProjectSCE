from scipy import stats

def PointsFromLines(listsofpoints):
	def LineInterception(l1,l2):
		w = int(-(l2[1]-l1[1])/(l2[0]-l1[0]))
		h = int(l1[0]*w+l1[1])
		return [w,h]
	
	lines = []
	
	for p in listsofpoints:
		slope,intercept,r_value, p_value, std_err = stats.linregress(p)
		lines.append([slope,intercept])
	
	p13 = LineInterception(lines[0],lines[2])
	p14 = LineInterception(lines[0],lines[3])
	p23 = LineInterception(lines[1],lines[2])
	p24 = LineInterception(lines[1],lines[3])

	return [p13,p14,p23,p24]
	
""" teted function: PointsFromLines, test date: 16/5/17, status: OK
#slope,intercept,r_value, p_value, std_err = stats.linregress([[10,245],[17,240],[150,251],[214,280],[440,240],[510,239]])

hu = [[10,10],  [17,15],  [150,54], [214,5],  [440,17], [510,7]  ]
hd = [[100,450],[170,430],[250,443],[314,445],[440,479],[510,427]]
vl = [[10,450], [17,430], [25,320], [31,150], [44,70],  [51,10]]
vr = [[510,50], [517,120],[525,240],[531,350],[544,410],[651,470]]

P = [hu,hd,vl,vr]

print PointsFromLines(P)


PI = []

for p in P:
	slope,intercept,r_value, p_value, std_err = stats.linregress(p)
	PI.append([slope,intercept])

#print PI

def interP(PI):
	def inter(l1,l2):
		w = int(-(l2[1]-l1[1])/(l2[0]-l1[0]))
		h = int(l1[0]*w+l1[1])
		return [w,h]
	p13 = inter(PI[0],PI[2])
	p14 = inter(PI[0],PI[3])
	p23 = inter(PI[1],PI[2])
	p24 = inter(PI[1],PI[3])
	return [p13,p14,p23,p24]

print interP(PI)
"""
