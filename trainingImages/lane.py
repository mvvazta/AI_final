import cv2
import numpy as np

laneLines = cv2.imread('laneLines.jpg') #1
laneBU = np.copy(laneLines)
grayScale = cv2.cvtColor(laneBU, cv2.COLOR_RGB2GRAY) #2
blur = cv2.GaussianBlur(grayScale, (5, 5), 0) #3
canny = cv2.Canny(blur, 50, 150)
cv2.imshow('result', canny)
cv2.waitKey(0)