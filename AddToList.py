def AddToList(lists, points, linenum):
	for p in points:
		lists[linenum-1].append(p)
	return lists

""" tested function: AddToList, test date: 15/5/17, status: OK  
P = [[[3,2], [4, 6], [3, 6]], [[1,1], [5, 6], [7, 6]], [[3,8], [7, 2], [9, 1]], [[8,4], [2, 0], [1, 1]]]
points1 = [[11,13], [113, 162], [533, 467]]
points2 = [[13,13], [103, 182], [5353, 467]]
points3 = [[12,13], [2, 13], [543, 437]]
points4 = [[10,14], [13, 167], [53, 47]]
AddToList(P[0],points1)
AddToList(P[1],points2)
AddToList(P[2],points3)
AddToList(P[3],points4)
print ""
for p in P:
    print p
"""

