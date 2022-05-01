import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

start = -10
finish = 11
shape = finish - start
n = np.arange(start, finish, 1)
xn = sig.unit_impulse(shape, (shape//2)-2) + sig.unit_impulse(shape, (shape//2)+1) + sig.unit_impulse(shape, (shape//2)+2)
plt.stem(n, xn)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.xticks(n)
plt.title('x[n]')
plt.show()

yn = 2*(sig.unit_impulse(shape, (shape//2) +2)) - sig.unit_impulse(shape, (shape//2) +1)
plt.stem(n, yn)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.xticks(n)
plt.title('y[n]')
plt.show()

zn = np.convolve(xn, yn, 'same')
plt.stem(n, zn)
plt.xlabel('n')
plt.ylabel('z[n]')
plt.xticks(n)
plt.title('z[n]')
plt.show()
