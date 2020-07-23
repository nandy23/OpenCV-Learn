import cv2
import numpy as np

# baca gambar
img = cv2.imread('lena.png')

#cv2.imshow("coba", img)
# cv2.waitKey(0)

kernel = np.ones((5, 5), np.uint8)

# print(kernel)

img_abu = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# angka blur tidak boleh genap
img_blur = cv2.GaussianBlur(img_abu, (9, 9), 0)
img_Canny = cv2.Canny(img, 220, 150)
img_Dialation = cv2.dilate(img_Canny, kernel, iterations=2)
img_eronded = cv2.erode(img_Dialation, kernel, iterations=1)

cv2.imshow("coba", img)
cv2.imshow("coba2", img_abu)
cv2.imshow("coba3", img_blur)
cv2.imshow("coba4", img_Canny)
cv2.imshow("coba5", img_Dialation)
cv2.imshow("coba6", img_eronded)
cv2.waitKey(0)
