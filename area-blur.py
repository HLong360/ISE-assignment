# https://www.youtube.com/watch?v=2Bz-aastGk0

from PIL import Image, ImageFilter

def cropping(image, cor):
    cropped_image = image.crop(cor)
    return cropped_image

def blur(image):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=1.5))
    return blurred_image


image = Image.open('result/cartoon.jpg')
portal = Image.open('img/portal.png')
image.paste(portal, (845,361,1606,1707))

smoke = Image.open('result/brighten-1.png') 
image.paste(smoke, (0,293,2560,1707), mask=smoke)
image.show()

image.save('result/portal-smoke.jpg')