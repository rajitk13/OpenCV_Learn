import cv2 as cv
import matplotlib.pyplot as plt

# RBG IS COLOR SPACE , CMYK EG ARE COLOR SPACES

img = cv.imread('Photos/cats.jpg')

# cv.imshow('cat', img)
#
# plt.imshow(img)
# plt.show()

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
#
# # BGR to HSV
HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', HSV)
#
# # BGR to LAB
#
# LAB = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', LAB)

# BGR TO Rgb

# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', rgb)

# we can convert all the color formats into each other but
# we cannot convert grayscale to hsv directly

# HSV TO BGR
hsv_bgr = cv.cvtColor(HSV, cv.COLOR_HSV2BGR)
cv.imshow('HSV', hsv_bgr)

# LAB TO BGR
# similar to above code from lab to bgr
cv.waitKey(0)

# BGR IS THE OPPOSITE OF RBG
# by default opencv uses BGR
