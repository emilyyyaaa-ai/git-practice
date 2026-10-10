import numpy as np
import matplotlib.pyplot as plt

# 1. 准备模拟数据
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([2.1, 4.3, 5.8, 8.2, 9.7, 12.3, 14.1, 15.9, 18.2])

# 2. 线性回归 y = w*x + b，计算权重w和偏置b
w, b = np.polyfit(x, y, deg=1)
print(f"拟合结果：y = {w:.2f} * x + {b:.2f}")

# 3. 绘制原图与拟合直线
plt.scatter(x, y, color='blue', label='原始数据')
plt.plot(x, w*x + b, color='red', label='AI拟合直线')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("简单AI线性回归演示")
plt.show()