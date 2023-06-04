import cv2

img = cv2.imread("./myEar.jpg")
h, w, _ = img.shape
h_n = 720
w_n = int(w * h_n * 1.0 / h )
img = cv2.resize(img, (w_n, h_n))
cv2.imwrite("./myEar0.jpg", img)

