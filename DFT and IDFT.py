import numpy as np
import cmath
from matplotlib import pyplot as plt


# this is 3 and 4 and 6


def unit_step(a, n):  # define unit step function
    unit = []
    for sample in n:
        if sample < a:
            unit.append(0)
        else:
            unit.append(1)
    return unit


def dft(x):  # get signal as list
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)  # exponent
    X = np.dot(e, x)
    return X


def idft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(2j * np.pi * k * n / N)
    X = np.dot(e, x) / N
    return X


start = -20
finish = 20
n = np.arange(start, finish, 1)
unit1 = unit_step(a=0, n=n)
unit2 = unit_step(a=5, n=n)
x1 = [unit1 - unit2 for unit1, unit2 in zip(unit1, unit2)]
x1 = x1[start:start + 5]
x2 = [1 for x in range(5)]
print(x1, x2)
x1w = dft(x1)
x2w = dft(x2)
print(x1w)
print('--------------------------')
print(x2w)
x3w = x1w * x2w
print('--------------------------')
print(x3w)
print('--------------------------')
x3 = idft(x3w)
print(np.real(x3))
x3 = np.pad(x3, (abs(start), abs(start)-5), mode='constant')
x3 = np.real(x3)
plt.stem(n,x3)
plt.xticks(n)
plt.show()