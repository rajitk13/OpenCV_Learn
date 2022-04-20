import cv2
import cv2 as cv

vid = cv2.VideoCapture(0)
vid.set(3, 640)  # set Width
vid.set(4, 480)  # set Height
haar_cascade = cv.CascadeClassifier('haar_face.xml')

while vid.isOpened():

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_rect = haar_cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=1, minSize=(20, 20))
    for (x, y, w, h) in frame_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

cv.waitKey(100)
