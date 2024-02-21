import cv2 
import numpy as np 


#5. Find clues:
def adjust_brightness_contrast(image, alpha=1.5, beta=25):
    """
    Adjust the brightness and contrast of an image.
    :param image: Input image.
    :param alpha: Controls the contrast (1.0 means no change).
    :param beta: Controls the brightness.
    :return: Adjusted image.
    """
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted_image

#Shadow effect
def add_shadow(image, intensity=0.5):
    """
    Add a shadow effect to an image.
    :param image: Input image.
    :param intensity: Shadow intensity (0 to 1).
    :return: Image with added shadow.
    """
    shadow = np.ones_like(image, dtype=np.float32) * intensity * 255
    result = cv2.subtract(image, shadow.astype(image.dtype))
    return result

#Saturation
def adjust_saturation(image, factor=1.5):
    """
    Adjust the saturation of an image.
    :param image: Input image.
    :param factor: Saturation adjustment factor (>1 increases saturation, <1 decreases saturation).
    :return: Image with adjusted saturation.
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * factor, 0, 255)
    result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return result

#Combining multiple colour channels
def split_channels_and_combine(image):
    """
    Split color channels, apply different effects, and combine them back.
    :param image: Input image.
    :return: Image with combined color channels.
    """
    b, g, r = cv2.split(image)

    # Example: Enhance the blue channel
    enhanced_b = cv2.equalizeHist(b)

    # Combine the enhanced blue channel with the original green and red channels
    combined_image = cv2.merge([enhanced_b, g, r])

    return combined_image

# Load an image
original_image = cv2.imread("Kheops-Pyramid.jpg")

# Adjust brightness and contrast
adjusted_image = adjust_brightness_contrast(original_image)
cv2.imwrite("img0.jpg", adjusted_image)

# Add shadow effect
image_with_shadow = add_shadow(original_image, intensity=0.5)
cv2.imwrite("img3.jpg", image_with_shadow)

image_sat = adjust_saturation(original_image)
cv2.imwrite("img1.jpg", image_sat)

# Split channels, apply effects, and combine
combined_channels_image = split_channels_and_combine(original_image)

# Display the results
# cv2.imshow("Original Image", original_image)
# cv2.imshow("Adjusted Image", adjusted_image)
# cv2.imshow("Image with Shadow", image_with_shadow)
# cv2.imshow("adjust saturation", image_sat)
# cv2.imshow("Combined Channels Image", combined_channels_image) 
cv2.waitKey(0)
cv2.destroyAllWindows()
