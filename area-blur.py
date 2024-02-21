# https://www.youtube.com/watch?v=2Bz-aastGk0

from PIL import Image, ImageFilter

def cropping(image, cor):
    cropped_image = image.crop(cor)
    return cropped_image

def blur(image):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=2))
    return blurred_image

# image.paste(blurred_image, (1,819,1579,969))
image = Image.open('result/bright1.jpg')
inner = cropping(image, (300,190,373,264))
# inner.save('result/inner.jpg')

image = Image.open('result/bright2.jpg')
mid = cropping(image, (181,56,492,366))
# mid.save('result/mid.jpg')

image = Image.open('result/bright3.jpg')
image.paste(mid, (181,56,492,366))
image.paste(inner, (300,190,373,264))
# image.save('result/red.png')
image.show()

image = Image.open('result/red.png')
light = Image.open('img/red-light.png')
image.paste(light, (312,202,362,252))
image.save('result/red-light-scene.jpg')
cropped = cropping(image,(300,190,373,264))
blurred = blur(cropped)
image.paste(blurred, (300,190,373,264))
image.save('result/red-light-scene-blur.jpg')
image.show()

