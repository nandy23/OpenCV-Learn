import cv2

width = 640
height = 480

capture = cv2.VideoCapture('test_video.mp4')

while True:
    success, img = capture.read()
    # resize (gambar, tuple dari lebar dan tinggi)
    img = cv2.resize(img, (width, height))
    cv2.imshow('hasil', img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

#cv2.imshow("hasil", img)
# cv2.waitKey(0)
# print(capture.read())
