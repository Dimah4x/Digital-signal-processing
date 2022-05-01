import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

def shiftx(z):
    return signal.unit_impulse(len(z), len(z)//2 - 2) + signal.unit_impulse(len(z), len(z)//2 + 1) + signal.unit_impulse(len(z), len(z)//2 + 2)

n = np.linspace(-4, 4, 9)
x = shiftx(n)
f = plt.stem(n, x)
plt.show()
x_coef = [-1, 2]
y_coef = [1]
y = signal.lfilter(x_coef, y_coef, x)
print(y)
f = plt.stem(n, y)
print(f)
for i in range(len(y)):
    y[i] = float(round(y[i], 2))
print(y)
plt.show()
