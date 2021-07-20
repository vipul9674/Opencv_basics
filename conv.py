import cv2
import numpy as np

image = cv2.imread('messi.jpg')

kernel = np.float32([[1, 1, 0],
                    [10, 0, -10],
                    [1, 1, -2]])

conv_image = cv2.filter2D(image, -1, kernel)

cv2.imshow("Conv", conv_image)
cv2.waitKey(0)