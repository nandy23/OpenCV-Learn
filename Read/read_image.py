import cv2

# load image
read_img = cv2.imread('lena.png')

# menampilkan gambar
cv2.imshow("Lena", read_img)
cv2.waitKey(0)
