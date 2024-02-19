# 图像的形态学算法（腐蚀和膨胀）
import cv2
import numpy as np

# 在腐蚀和膨胀之前需要先将图片二值化
gray = cv2.imread("opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)  # 使用反向阈值——背景白色，图案黑色
kernel = np.ones((5, 5), np.uint8)  # 操作需要用到的kernel

# 腐蚀和膨胀操作
erosion = cv2.erode(binary, kernel)
dilation = cv2.dilate(binary, kernel)

cv2.imshow("binary", binary)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)


cv2.waitKey()
