import numpy as np
import matplotlib.pyplot as plt

x = np.ones((3,3)) + np.arange(3)
print(x)



###########__2__##########
# x = np.random.multivariate_normal([0,0], [[1,2],[2,5]],100)
# indices = np.random.choice(100, size=10)
# print(indices)
# plt.scatter(x[:,0], x[:,1], s=3)
# plt.scatter(x[indices, 0], x[indices, 1], fc="none", ec="k")
# plt.show()


##########__1__######
# # pole x a y pro vykreesleni
# x = np.linspace(0, 4 * np.pi, 1000)
# y = np.sin(x)

# neg = (np.mod(x, np.pi * 2) > np.pi) | (y > 0.5)

# plt.plot(x[~neg], y[~neg], c="tab:red")

# y2 = y.copy()
# y2[~neg] = np.nan

# plt.plot(x, y2, c="tab:blue", ls=":")
# plt.show()

# print(neg)
###############


