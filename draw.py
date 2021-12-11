import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')

# Creating a blank image

blank = np.zeros((500, 500, 3), dtype='uint8')
# Changing color of blank
# blank[:] = 0, 0, 255

# Painting a range of blank image
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Blank', blank)

# Draw a Rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# cv.imshow('Blank', blank)

# TO FILL RECTANGLE THICKNESS - cv.FILLED / -1

# ALTERNATE METHOD OF CREATING A RECTANGLE

# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=-1)
# cv.imshow('Blank', blank)
# Creating Circle

# cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=3)
# cv.imshow('Circle', blank)

# Draw a line
# cv.line(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# Writing Text on a image
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)
