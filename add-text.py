# https://www.geeksforgeeks.org/adding-text-on-image-using-python-pil/

# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open('result/fusion_mertens.jpg')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype('ITCBLKAD.TTF', 80)

# Add Text to an image
I1.text((30, 15), "Paris, France", font=myFont, fill =(240, 30, 30))

# Display edited image
img.show()

# Save the edited image
img.save("result/paris.jpg")