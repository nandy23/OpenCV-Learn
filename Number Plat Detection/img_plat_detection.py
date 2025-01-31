import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
img = cv2.imread("plat.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Hasil", img)
cv2.waitKey(0)
