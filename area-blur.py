# https://www.youtube.com/watch?v=2Bz-aastGk0

from PIL import Image, ImageFilter

image = Image.open('Kheops-Pyramid.jpg')
# image.show()

cropped_image = image.crop((1,819,1579,969))
blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius=2))
image.paste(blurred_image, (1,819,1579,969))
cropped_image.show()
blurred_image.show()
image.show()