import cv2

width = 640
height = 480

capture = cv2.VideoCapture(0)
capture.set(3, width)
capture.set(4, height)
capture.set(10, 150)
while True:
    success, img = capture.read()
    cv2.imshow("hasil", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
