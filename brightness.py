from PIL import Image, ImageEnhance

img = Image.open("img/Machu Picchu/machu-6.jpg")
enhancer = ImageEnhance.Brightness(img)
# to reduce brightness by 50%, use factor 0.5
img = enhancer.enhance(0.7)

img.show()
img.save("result/darken.jpg")