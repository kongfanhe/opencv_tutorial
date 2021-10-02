
import cv2

gray = cv2.imread("opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(gray, cv2.CV_64F)
canny = cv2.Canny(gray, 100, 200)

cv2.imshow("gray", gray)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)

cv2.waitKey()

