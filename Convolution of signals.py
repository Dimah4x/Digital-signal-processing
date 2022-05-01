import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import pandas as pd

def unit_step(a, n): #define unit step function
    unit = []
    for sample in n:
        if sample < a:
            unit.append(0)
        else:
            unit.append(1)
    return unit

################################define x[n]###################################
a = -2
finish = 101
start = -100
shape = finish - start
n = np.arange(start, finish, 1)
unit1 = unit_step(a, n)
b = 30
unit2 = unit_step(b, n)
xn = [unit1 - unit2 for unit1, unit2 in zip(unit1, unit2)]
xn = [xn*2 for xn in xn]
plt.stem(n, xn)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(n)
plt.title('x[n]')
plt.show()
################################define h[n]###################################
c = 0
unit3 = unit_step(c, n)
d = 3
unit4 = unit_step(d, n)
imp1 = 0.5*(sig.unit_impulse(shape, (shape//2) + 35)) #works only if shape is symmetrical
hn = [unit3 - unit4 for unit3, unit4 in zip(unit3, unit4)]
hn = [hn + imp1 for hn, imp1 in zip(hn, imp1)]
plt.stem(n, hn)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.xticks(n)
plt.title('h[n]')
plt.show()
################################define y[n]###################################
yn = sig.convolve(xn, hn, 'same')
plt.stem(n, yn)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.xticks(n)
plt.title('y[n]')
plt.show()
