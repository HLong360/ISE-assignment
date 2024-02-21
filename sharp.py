#https://www.geeksforgeeks.org/image-enhancement-techniques-using-opencv-python/

#Import the necessary libraries 
import cv2 
import numpy as np 

# Load the image 
image = cv2.imread('result/paris.jpg') 

# Create the sharpening kernel 
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 

# Sharpen the image 
sharpened_image = cv2.filter2D(image, -1, kernel) 

#Save the image 
cv2.imwrite('result/sharpened_image_1.jpg', sharpened_image) 

cv2.imshow('Sharpened', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()