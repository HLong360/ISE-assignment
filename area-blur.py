# https://www.youtube.com/watch?v=2Bz-aastGk0

from PIL import Image, ImageFilter

def cropping(image, cor):
    cropped_image = image.crop(cor)
    return cropped_image

def blur(image):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=1.5))
    return blurred_image


image = Image.open('result/smoke-scene.png')
smoke = Image.open('result/brighten.png')
image.paste(smoke,(0,0,1200,663), mask=smoke)
# image.show()

blurred = blur(image)
# blurred.show()

blurred.save('result/blur.jpg')