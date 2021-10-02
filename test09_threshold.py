
import cv2

gray = cv2.imread("bookpage.jpg", cv2.IMREAD_GRAYSCALE)
ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
binary_adaptive = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("gray", gray)
cv2.imshow("binary", binary)
cv2.imshow("adaptive", binary_adaptive)
cv2.imshow("otsu", binary_otsu)

cv2.waitKey()

