import matplotlib.pyplot as plt
import numpy as np
# this is 7


def unit_step(a, n): #define unit step function
    unit = []
    for sample in n:
        if sample < a:
            unit.append(0)
        else:
            unit.append(1)
    return unit


start = -10
finish = 20
n = np.arange(start, finish)
unit1 = unit_step(a=0,n=n)
unit2 = unit_step(a=5,n=n)
x1 = [unit1-unit2 for unit1,unit2 in zip(unit1,unit2)]
x2 = [1 for x in range(5)]
y = np.convolve(x1, x2, 'full')
y = y[:finish-start]
plt.stem(n, y)
plt.xticks(n)
plt.show()
