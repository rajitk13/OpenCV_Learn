import cv2 as cv

img = cv.imread('Photos/cat.jpg')

# cv.imshow('Cat', img)

# Converting to grayscale

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
#
# cv.imshow('Blur',blur)

# Edge Cascade

canny = cv.Canny(img, 125, 175)
# cv.imshow('Edges', canny)

# Dilating the image
dilate = cv.dilate(canny, (3, 3), iterations=1)
# cv.imshow('dilated', dilate)

# Eroded image
eroded = cv.erode(dilate, (3, 3), iterations=1)
# cv.imshow('Erode', eroded)

# Resize

# resized = cv.resize(img, (500, 500))
# cv.imshow('Resized', resized)

# We use interpolation for better resizing and scaling

# Cropped
cropped = img[50:200, 200:400]
cv.imshow('Crop', cropped)
cv.waitKey(0)
