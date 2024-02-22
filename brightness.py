from PIL import Image, ImageEnhance

img = Image.open("img/smoke-2.png")
enhancer = ImageEnhance.Brightness(img)
# to reduce brightness by 50%, use factor 0.5
img = enhancer.enhance(2.5)

img.show()
img.save("result/brighten.png")