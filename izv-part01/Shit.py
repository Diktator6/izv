import matplotlib.pyplot as plt
import numpy as np

x1,x2,x3,y1,y2,y3= (1,2,3,4,5,6)

plt.figure(figsize=(6,4))
plt.subplot(2,1,1)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.subplot(2,1,2)
plt.plot(x3,y3)
#plt.savefig("plot.png")
plt.show()

x = np.arange(0, 2*np.pi, 0.1)
plt.plot(x, np.sin(x), 'C3', label='plot 1')
plt.xlabel('time (s)')
plt.ylabel('voltage (V)')
plt.title('My plot')
plt.legend()
plt.show()