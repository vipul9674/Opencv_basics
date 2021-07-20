import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
	success,frame = cap.read()
	if success:
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('gFrame',gray_frame)
		cv2.imshow('Frame',frame)
		k = cv2.waitKey(100)
		if k & 0xff == ord('a'):
			break
	else:
		break
