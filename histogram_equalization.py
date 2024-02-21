import cv2 
import numpy as np 

def histogram_equalization(image):
    # Split the image into its RGB channels
    b, g, r = cv2.split(image)
    
    # Apply histogram equalization to each channel separately
    b_equalized = cv2.equalizeHist(b)
    g_equalized = cv2.equalizeHist(g)
    r_equalized = cv2.equalizeHist(r)
    
    # Merge the equalized channels back into a BGR image
    equalized_image = cv2.merge((b_equalized, g_equalized, r_equalized))
    
    # Display the original and equalized images
    # cv2.imshow('Original Image', image)
    cv2.imshow('Equalized Image', equalized_image)

    cv2.imwrite('result/hist.jpg', equalized_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread('img/Eiffel Tower/eiffel-tower-2.jpg') 
histogram_equalization(image)
