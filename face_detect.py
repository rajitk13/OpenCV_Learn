import cv2
import cv2 as cv

vid = cv2.VideoCapture(0)
# vid.set(3, 640)  # set Width
# vid.set(4, 480)  # set Height
# haar_cascade = cv.CascadeClassifier('haar_face.xml')

img = cv.imread('Photos/group 2.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv2.imshow('Gray Person', gray)
haar_cascade = cv.CascadeClassifier('haar_face.xml')


faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
# we can print faces_rect length to get the number of faces found

print(f"Number of faces found  = {len(faces_rect)}")
# haar cascades get the rectangular edges for the faces

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', img)
cv.waitKey(0)


