# COLOR CHANNELS
# how to split and merge color channels in opencv
# bgr and rbg are 3 color channels merged together
# in open cv we can split color into there color channels

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

bluemerge = cv.merge([b, blank, blank])

cv.imshow('blue_blank', bluemerge)

# Merging these color channels together

Merged = cv.merge([b, g, r])

cv.imshow('Merged Image', Merged)

cv.waitKey(0)
