import cv2 as cv


def rescaleframe(Frame, scale=0.2):
    width = int(Frame.shape[1] * scale)
    height = int(Frame.shape[0] * scale)

    dimension = (width, height)

    return cv.resize(Frame, dimension, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
    # Alternate methode of changing res
    # Changes res of LIVE VIDEO only
    dimension = (width, height)



capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleframe(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()

cv.waitKey(0)
