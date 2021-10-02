
import cv2

print(cv2.getVersionString())

image = cv2.imread("opencv_logo.jpg")
print(image.shape)


cv2.imshow("image", image)
cv2.waitKey()

