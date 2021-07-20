import cv2
import numpy as np

canvas = np.zeros((512,512,3), np.uint8)
cv2.line(canvas, (0,0),(511,511),(255,0,0),3)
cv2.rectangle(canvas, (100,100),(300,300),(0,100,250),3)
cv2.putText(canvas,"Over 9000",(100,150),cv2.FONT_HERSHEY_SIMPLEX ,1,(0,10,200),4)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)