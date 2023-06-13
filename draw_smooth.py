# 用平滑曲线连接散点

x = (0.2, 0.6, 1.1, 1.5, 1.9, 2.8, 3.5, 4.1, 4.7, 5.4, 6.0, 6.4)
y = (38.93, 31.83, 32.32, 32.56, 35.5, 30.12, 31.83, 35.99, 35.74, 35.01, 36.97, 36.72)

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline

x = np.array(x)
y = np.array(y)
x_smooth = np.linspace(
    x.min(), x.max(), 300
)  # np.linspace 等差数列,从x.min()到x.max()生成300个数，便于后续插值
y_smooth = make_interp_spline(x, y)(x_smooth)
plt.plot(x_smooth, y_smooth)
plt.show()
