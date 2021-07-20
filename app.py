import cv2
import numpy as np
image=cv2.imread('messi.jpg')
print(image)
height,width,channels= image.shape

M=np.float32([[0,1,50],[2,0,50]])
rotated_matrix = cv2.getRotationMatrix2D((height/2,width/2),90,1)
translated_image= cv2.warpAffine(image,M,(height,width))

rotated_image= cv2.warpAffine(image,rotated_matrix,(height,width))
scale_image= cv2.resize(image,None,fx=3 ,fy=1.5)
cv2.imshow("Image",image)
cv2.imshow("translated Image",translated_image)
cv2.imshow("rotated Image",rotated_image)
#cv2.imwrite("Rotated.jpg",rotated_image)
cv2.imshow("scale Image",scale_image)
cv2.waitKey(0)