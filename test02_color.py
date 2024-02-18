# 图像的颜色
import cv2

image = cv2.imread("opencv_logo.jpg")
# 颜色通道顺序：BGR
cv2.imshow("blue", image[:, :, 0])
cv2.imshow("green", image[:, :, 1])
cv2.imshow("red", image[:, :, 2])

# 彩色图片灰度化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

cv2.waitKey()

