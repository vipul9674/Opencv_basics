import cv2 

cap =cv2.VideoCapture(0)
#image= cv2.imread("messi.jpg")
image2 = cv2.imread("italy.png")

while True:
	flag, frame = cap.read()
	if not flag:
		print("could not access the webcam")
		break

#	image= cv2.resize(image, (frame.shape[1],frame.shape[0]))
	image2= cv2.resize(image2, (frame.shape[1],frame.shape[0]))
#	img=image +image2
	blended_frame=cv2.addWeighted(frame,0.5,image2,0.5,gamma=0.1)
	cv2.imshow("Blended Image",blended_frame)
	if cv2.waitKey(10) &0xff == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()