import cv2
import numpy as np
image1 =cv2.imread("barca.jpg")
image2 = cv2.imread('messi.jpg')
image2 =cv2.resize(image2, (image1.shape[1],image1.shape[0]))
add_img=image1+image2

blended_image=cv2.addWeighted(image1,0.7,image2,0.3,gamma=0.5)

cv2.imshow("Blended Image",blended_image)
cv2.imshow("Added Image",add_img)
cv2.waitKey(0)