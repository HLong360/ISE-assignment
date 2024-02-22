from PIL import Image, ImageEnhance

img = Image.open("result/smoke-scene.png")
enhancer = ImageEnhance.Brightness(img)
# to reduce brightness by 50%, use factor 0.5
img = enhancer.enhance(0.7)

img.show()
# img.save("result/brighten.png")