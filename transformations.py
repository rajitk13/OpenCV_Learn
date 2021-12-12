# BASIC IMAGE TRANSFORMATION

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')

# Translation
# cv.imshow('Boston', img)
#
#
# def translate(image, x, y):
#     transMat = np.float32([[1, 0, x], [0, 1, y]])
#     dimensions = (image.shape[1], image.shape[0])
#     return cv.warpAffine(image, transMat, dimensions)
#
#
# # -x -->>left
# # -y -->>up
# # x -->>right
# # y -->>down
#
# translated = translate(img, 100, 100)

# cv.imshow('translate', translated)

# Rotation
# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
#     if rotPoint is None:
#         rotPoint = (width // 2, height // 2)
#
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)
#     return cv.warpAffine(img, rotMat, dimensions)
#
#
# rotated = rotate(img, 45)
#
# cv.imshow('Rotated', rotated)

# Resizing
#
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
#
# cv.imshow('Resized', resized)

# Flipping

# flip = cv.flip(img, 0)
#
# cv.imshow('Flipped', flip)

# Cropping

crop = img[200:400, 300:400]
cv.imshow('cropped', crop)
cv.waitKey(0)
