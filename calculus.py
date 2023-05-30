import numpy as np
import matplotlib.pyplot as plt

a1 = np.random.randn(100)*10 +100

mean = np.mean(a1)

std = np.std(a1)

print(np.percentile(a1, 70))

# print(mean,std)
# print(a1)
