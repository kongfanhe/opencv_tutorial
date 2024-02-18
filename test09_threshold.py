# 图片的阈值算法(二值化，将连续的灰度范围切割为白+黑)
import cv2

# 图片灰度二值化
gray = cv2.imread("bookpage.jpg", cv2.IMREAD_GRAYSCALE)
ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
# 图片自适应二值化（划分区块二值化，效果更好）
binary_adaptive = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
# 大津算法（基于图片灰度聚类分析，自定义阈值）
ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("gray", gray)
cv2.imshow("binary", binary)
cv2.imshow("adaptive", binary_adaptive)
cv2.imshow("otsu", binary_otsu)
cv2.waitKey()

# ret/ret1是一个浮点数，表示图像中像素值的阈值
print(ret)
print(ret1)
