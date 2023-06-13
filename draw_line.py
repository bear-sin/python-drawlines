# 根据散点拟合出一条直线
# 引用库函数
import numpy as np
import matplotlib.pyplot as plt

x = np.array([2.90, 3.249, 3.614, 3.324, 3.578, 3.757])
y = np.array([0.039, 0.0499, 0.0673, 0.0763, 0.1067, 0.1385])

# 计算回归系数
slope, intercept = np.polyfit(x, y, 1)  # 分别是斜率和截距
print(slope)  # 斜率
print(intercept)  # 截距
# 绘制拟合曲线
plt.scatter(x, y)
plt.plot(x, slope * x + intercept, color="red")

plt.show()
