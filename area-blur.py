# https://www.youtube.com/watch?v=2Bz-aastGk0

from PIL import Image, ImageFilter

def cropping(image, cor):
    cropped_image = image.crop(cor)
    return cropped_image

def blur(image):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=2))
    return blurred_image

# image.paste(blurred_image, (1,819,1579,969))

image = Image.open('img/Machu Picchu/machu-1.png')
smoke = Image.open('result/brighten.png')
image.paste(smoke,(0,177,1200,840), mask=smoke)
image.save('result/smoke-scene.png')


