# BASIC IMAGE TRANSFORMATION

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')

cv.imshow('Boston', img)


def translate(image, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)


# -x -->>left
# -y -->>up
# x -->>right
# y -->>down

translated = translate(img, 100, 100)

cv.imshow('translate', translated)
cv.waitKey(0)