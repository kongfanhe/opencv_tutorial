# opencv调用电脑中的摄像头
import cv2

# 获取摄像头设备的指针(设备管理器 -> 照相机)
capture = cv2.VideoCapture(0)
ret = True

# 摄像头的读取是连续不断的，需要循环读取
while ret:
    ret, frame = capture.read()
    '''
    ret：这是一个布尔值，表示读取操作是否成功。
    如果 ret 为 True，表示成功读取了一帧图像；如果为 False，则表示读取失败，可能是因为视频流结束或者其他错误。
    在处理视频流时，这个返回值通常用于控制循环，直到视频流结束。

    frame：这是一个NumPy数组，代表了从视频捕获对象读取的当前帧。
    这个数组通常是一个三维的，其形状为 (高度, 宽度, 通道数)，其中通道数可以是1（灰度图像）或3（彩色图像，分别对应红、绿、蓝通道）。
    '''
    cv2.imshow("camera", frame)
    key = cv2.waitKey(1)  # 等待键盘输入1ms
    if key != -1:  # 按任意键跳出循环
        break

capture.release()  # 释放指针

