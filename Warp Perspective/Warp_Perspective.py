import cv2
import numpy as np

img = cv2.imread('cards.jpg')

width, height = 250, 350

posisi1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])

posisi2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# print(posisi1)

# print()

# print(posisi2)

matrix = cv2.getPerspectiveTransform(posisi1, posisi2)
img_output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Asli", img)
cv2.imshow("Hasil", img_output)

cv2.waitKey(0)
