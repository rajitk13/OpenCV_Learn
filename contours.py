import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
blank = np.zeros(img.shape, dtype='uint8')

# img = cv.imread('Photos/cats.jpg')

# cv.imshow('cats', img)
#
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
# cv.imshow('grAY',gray)
#
canny = cv.Canny(img,125,175)
# cv.imshow('canny',canny)
#
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contours found ')
# We can blur the image to reduce the contours

# Another way of finding the contour , that is threshold

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# below 125 black and above 255 white

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
# Contours are not same as edges in canny but yeah they are sort of same

cv.imshow('Contours Drawn', blank)
cv.waitKey(0)
