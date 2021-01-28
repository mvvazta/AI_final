import cv2
import numpy as np
import matplotlib.pyplot as plt #5

def cannyStep(image):
		grayScale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #2
		blur = cv2.GaussianBlur(grayScale, (5, 5), 0) #3
		canny = cv2.Canny(blur, 50, 150) #4
		return canny

def showLines(image, lines):
	lineImg = np.zeros_like(image)
	if lines is not None:
		for line in lines:
			x1, y1, x2, y2 = line.reshape(4)
			cv2.line(lineImg, (x1, y1), (x2, y2), (255, 0, 0), 10)

	return lineImg

def regionMask(image): #6
	height = image.shape[0]
	#[(200, height), (1100, height), (550, 250)] for ll 4 and 5
	regions = np.array([
		[(310, height), (775, height), (775, 180), (442, 0), (366, 0)]
		])
	mask = np.zeros_like(image)
	cv2.fillPoly(mask, regions, 255)
	maskedImage = cv2.bitwise_and(canny, mask) #7
	return maskedImage

laneLines = cv2.imread('laneLines.jpg') #1
laneBU = np.copy(laneLines)

canny = cannyStep(laneBU)
croppedImage = regionMask(canny)

lines = cv2.HoughLinesP(croppedImage, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5) #8

lineDrawed = showLines(laneBU, lines)

mergedImage = cv2.addWeighted(laneBU, 0.8, lineDrawed, 1, 1)

# plt.imshow(canny)
# plt.show()
cv2.imshow('region', mergedImage)
cv2.waitKey(0)