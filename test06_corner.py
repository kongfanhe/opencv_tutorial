# 图片特征的提取
import cv2

image = cv2.imread("opencv_logo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 图片先灰度化

# 获取特征点 （对象， 最多的点数， 质量优度水平， 特征点之间的最小距离）
corners = cv2.goodFeaturesToTrack(gray, 500, 0.1, 10)
# 标记出每个点
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (int(x), int(y)), 3, (255, 0, 255), -1)

cv2.imshow("corners", image)
cv2.waitKey()
# 可以发现，特征点主要都在图片的转角处


