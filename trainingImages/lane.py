import cv2
import numpy as np
import matplotlib.pyplot as plt #5


def makeCoords(image, lineParam):
	slope, inter = lineParam
	y1 = image.shape[0]
	y2 = int(y1*(3/5))
	x1 = int((y1 - inter) / slope)
	x2 = int((y2 - inter) / slope)
	return np.array([x1, y1, x2, y2])

def avgSlope(image, lines):
	leftLift = []
	rightLift = []
	for line in lines:
		x1, y1, x2, y2 = line.reshape(4)
		param = np.polyfit((x1, x2), (y1, y2), 1)
		slope = param[0]
		inter = param[1]
		if slope < 0:
			leftLift.append((slope, inter))
		else:
			rightLift.append((slope, inter))
	leftLiftAvg = np.average(leftLift, axis=0)
	rightLiftAvg = np.average(rightLift, axis=0)
	leftLine = makeCoords(image, leftLiftAvg)
	rightLine = makeCoords(image, rightLiftAvg)
	return np.array([leftLine, rightLine])


def cannyStep(image):
		grayScale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #2
		blur = cv2.GaussianBlur(grayScale, (5, 5), 0) #3
		canny = cv2.Canny(blur, 50, 150) #4
		return canny

def showLines(image, lines):
	lineImg = np.zeros_like(image)
	if lines is not None:
		for x1, y1, x2, y2 in lines:
			cv2.line(lineImg, (x1, y1), (x2, y2), (255, 0, 0), 10)

	return lineImg

def regionMask(image): #6
	height = image.shape[0]
	#[(200, height), (1100, height), (550, 250)] for ll 4 and 5
	#[(377, height), (775, height), (775, 180), (442, 0), (375, 0)]
	regions = np.array([
		[(200, height), (1100, height), (550, 250)]
		])
	mask = np.zeros_like(image)
	cv2.fillPoly(mask, regions, 255)
	maskedImage = cv2.bitwise_and(image, mask) #7
	return maskedImage

# laneLines = cv2.imread('laneLines5.jpg') #1
# laneBU = np.copy(laneLines)

#plt.imshow(canny)
#plt.show()

capture = cv2.VideoCapture("../trainingVideo/laneLinesVid.mp4")

while(capture.isOpened()):
	_, frame = capture.read()
	canny = cannyStep(frame)
	croppedImage = regionMask(canny)

	linesC = cv2.HoughLinesP(croppedImage, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5) #8

	avgLines = avgSlope(frame, linesC) #10

	lineDrawed = showLines(frame, avgLines)

	mergedImage = cv2.addWeighted(frame, 0.8, lineDrawed, 1, 1) #9
	cv2.imshow('region',mergedImage)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
capture.release()
cv2.destroyAllWindows()