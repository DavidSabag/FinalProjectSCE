def CheckPoints(cropframe, points):
    H, W = cropframe.shape[0],  cropframe.shape[1]
    for w, h in points:
        if w < 0 or w > W or h<0 or h>H:
            return False
    if points[2][0] < points[0][0] and points[0][0] < points[1][0] and points[1][0] < points[3][0]:
        return True
    return False
