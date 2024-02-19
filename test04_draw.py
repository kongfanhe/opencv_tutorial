# 实现绘图功能
import cv2
import numpy as np

# 创建黑色画布
image = np.zeros([300, 300, 3], dtype=np.uint8)

# 绘制线段（对象， 起点， 终点， 颜色， 粗细）
cv2.line(image, (100, 200), (250, 250), (255, 0, 0), 2)
# 绘制矩形（~，起点， 对角点， 颜色， 粗细）
cv2.rectangle(image, (30, 100), (60, 150), (0, 255, 0), 2)
# 绘制圆形（~，圆心， 半径， 颜色， 粗细）
cv2.circle(image, (150, 100), 20, (0, 0, 255), 3)
# 绘制字符串（~， 内容， 坐标， 字体格式序号， 缩放系数， 颜色， 粗细， 线条类型序号）
cv2.putText(image, "hello", (100, 50), 0, 1, (255, 255, 255), 2, 1)

cv2.imshow("image", image)
cv2.waitKey()
