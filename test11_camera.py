
import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv2.imshow("camera", frame)
    key = cv2.waitKey(1)
    if key != -1:
        break

capture.release()

