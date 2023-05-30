import numpy as np
import matplotlib.pyplot as plt

names = np.array(['Max','Paul','Ibrahim','Yury','James'])

print(np.vectorize(lambda s:s[0])(names)=='M')