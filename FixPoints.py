def FixPoints(points, fix):
    p1, p2, p3, p4 = points[0], points[1], points[2], points[3] 
    p1 = p1[0]+fix, p1[1]+fix
    p2 = p2[0]-fix, p2[1]+fix
    p3 = p3[0]+fix, p3[1]-fix
    p4 = p4[0]-fix, p4[1]-fix
    return [p1, p2, p3, p4]
