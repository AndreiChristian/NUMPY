import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([1,2,3])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0,10,100)

# print(a1>2)
# print(a1[a1>2])

x = np.linspace(0,1,100)
y = x**2

plt.plot(x,y)
plt.show()