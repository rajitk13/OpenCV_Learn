import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Original', img)
# we generally blur images when there are lighting issues and there is a lot of noise in
# the image, so we blur it

# Averaging
# average = cv.blur(img, (3, 3))
# # Higher the kernel size higher is the blur
# cv.imshow('Average Blue', average)

# Gaussian Blur
# Works same way as averaging but is more natural than averaging

# gauss = cv.GaussianBlur(img, (7, 7), 0)
# cv.imshow('Gaussian Blur', gauss)

# Median Blurring , effective in removing the noise , uses median of the pixels

# median = cv.medianBlur(img, 3)
# cv.imshow("Median Blur", median)

# Bilateral Blurring
bilateral = cv.bilateralFilter(img, 20, 35, 35)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)
