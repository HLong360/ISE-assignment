import cv2

# enhancing color in images

image = cv2.imread('img/Eiffel Tower/eiffel-tower-5.jpg')

def change(image, h, s, v):
    # convert the image from RGB to HSV color space
    image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    # adjust hue
    image[:, :, 0] = image[:, :, 0] * h

    # adjust saturation
    image[:, :, 1] = image[:, :, 1] * s

    # adjust value
    image[:, :, 2] = image[:, :, 2] * v

    cv2.imshow("Image", image) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return image

brightest = change(image, 0, 0.99, 0.99)
cv2.imwrite('result/bright1.jpg', brightest)
mid = change(image, 0, 0.99, 0.6)
cv2.imwrite('result/bright2.jpg', mid)
dark = change(image, 0, 0.99, 0.3)
cv2.imwrite('result/bright3.jpg', dark)
