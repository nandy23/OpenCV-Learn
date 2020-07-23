import cv2
import numpy as np

img = cv2.imread('lambo.png')

print(img.shape)
# untuk lebar dan tinggi, dimasukan kedalam tuple
img_risize = cv2.resize(img, (1000, 500))

print(img_risize.shape)

# 0:200 = mengambil data dari 0 smpe 200
# 200:500 = mengambil data dari 200 smpe 500
img_crop = img[0:200, 200:500]
cv2.imshow("Asli", img)
cv2.imshow("Img Risize", img_risize)
cv2.imshow("Img Crop", img_crop)

cv2.waitKey(0)
