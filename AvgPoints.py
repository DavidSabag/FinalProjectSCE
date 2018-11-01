def AvgPoints(points1, points2):
    points = [[0,0 ], [0, 0], [0, 0], [0,0 ]]
    for i in range(0, 4):
        points[i][0] = int((points1[i][0]+points2[i][0])/2)
        points[i][1] = int((points1[i][1]+points2[i][1])/2)
    return points
