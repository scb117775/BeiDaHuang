import cv2
import numpy as np

# 读取图片
image = cv2.imread('F:/1.jpg')

# 将图片转换为HSV颜色空间
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 设置背景色的HSV范围
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# 根据背景色的HSV范围创建掩膜
mask = cv2.inRange(hsv_image, lower_red, upper_red)

# 将掩膜应用到原始图片上
result = cv2.bitwise_and(image, image, mask=mask)

# 将背景色替换为红色
result[mask != 0] = [0, 0, 255]

# 显示结果图片
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()