# https://www.geeksforgeeks.org/adding-text-on-image-using-python-pil/

# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open('Kheops-Pyramid.jpg')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype('GIGI.TTF', 65)

# Add Text to an image
I1.text((10, 10), "Nice Pyramid", font=myFont, fill =(255, 0, 0))

# Display edited image
img.show()

# Save the edited image
# img.save("car2.png")
