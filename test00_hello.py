# 基本IO
import cv2
# 读取版本号
print(cv2.getVersionString())
# 读取图片
image = cv2.imread("opencv_logo.jpg")
# 打印图片的形状（高度，宽度，通道数）
print(image.shape)


cv2.imshow("image", image)
cv2.waitKey()  # 让窗口暂停

