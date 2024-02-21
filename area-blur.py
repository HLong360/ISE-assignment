# https://www.youtube.com/watch?v=2Bz-aastGk0

from PIL import Image, ImageFilter

image = Image.open('img/Eiffel Tower/eiffel-tower-4.jpg')

def cropping(image, cor):
    cropped_image = image.crop((1,819,1579,969))
    return cropped_image

def blur(image):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=2))
    return blurred_image

# image.paste(blurred_image, (1,819,1579,969))
blurred = blur(image)
blurred.show()