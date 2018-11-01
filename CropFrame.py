def CropFrame(frame):
	height,width = frame.shape[0],frame.shape[1]
	x1, x2 = height-int(0.6*height), height
	y1, y2 = 0, width
	return frame[x1:x2, y1:y2]
