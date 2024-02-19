# 图片的模板匹配（以匹配扑克牌上的菱形为例）
import cv2
import numpy as np

image = cv2.imread("poker.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 选取匹配模板
template = gray[75:105, 235:265]

# 使用标准相关匹配算法——将待检测对象和模板都标准化再来计算匹配度
match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
locations = np.where(match >= 0.9)  # 找出匹配系数大于0.9的匹配点

w, h = template.shape[0:2]
for p in zip(*locations[::-1]):  # 循环遍历每一个匹配点并画出矩形框标记
    x1, y1 = p[0], p[1]
    x2, y2 = x1 + w, y1 + h
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("image", image)
cv2.waitKey()


