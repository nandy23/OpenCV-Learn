import cv2
import numpy as np

# isi dari np.zeros menggunakan tuple
img = np.zeros((512, 512, 3), np.uint8)

# print(img)
#img[:] = 255, 0, 0

# print(img)

cv2.line(img, (0, 0), (img.shape[0], img.shape[1]), (0, 255, 0), 5)

cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 10)
cv2.circle(img, (450, 50), 30, (255, 255, 0), 5)

cv2.putText(img, "Belajar", (300, 200),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)

cv2.imshow("Tampil", img)
cv2.waitKey(0)
