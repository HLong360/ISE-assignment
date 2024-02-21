# https://stackoverflow.com/questions/60609607/how-to-create-this-barrel-radial-distortion-with-python-opencv

from wand.image import Image
import numpy as np
import cv2

with Image(filename='A_Famosa_Fortress.jpg') as img:
    print(img.size)
    img.virtual_pixel = 'transparent'
    img.distort('barrel', (0.2, 0.0, 0.0, 1.0))
    img.save(filename='checks_barrel.png')
    # convert to opencv/numpy array format
    img_opencv = np.array(img)

# display result with opencv
cv2.imshow("BARREL", img_opencv)
cv2.waitKey(0)