# From programming prospective gradients can be thought of
# as edges but they are not exactly same but yeah for the sake of ease
# it is considered as edges

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Laplacian edges , works through this computes the gradients of this image
# images do not have negative pixel value so we play with absolute values

# Sobel
# it computes in two directions x and y

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('Sobel x ', sobelx)
cv.imshow('Sobel y ', sobely)
# we combine the two

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

# therefore, canny is a multistage process therefore sobel is used in it
# just one of its process
cv.waitKey(0)
