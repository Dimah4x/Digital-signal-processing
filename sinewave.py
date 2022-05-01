import math
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 200, 1)

OMEGA_ZERO = 0.1
plt.xlabel("n")
plt.ylabel("f(n)")
plt.title('plot of cos(w0n)')
y1 = np.cos(OMEGA_ZERO*n)
plt.scatter(n, y1, label='cos(w0n)')
plt.legend(loc='lower right')
plt.show()

OMEGA_ONE = OMEGA_ZERO + 2*math.pi
plt.xlabel("n")
plt.ylabel("f(n)")
plt.title('plot of cos(w1n)+0.5')
y2 = [np.cos(n*OMEGA_ONE)+0.5]
plt.scatter(n, y2, label='cos(w1n)+0.5')
plt.legend(loc='lower right')
plt.show()

OMEGA_TWO = OMEGA_ZERO + 50*math.pi
plt.xlabel("n")
plt.ylabel("f(n)")
plt.title('plot of cos(w2n+1)')
y3 = [np.cos(OMEGA_TWO*n)+1]
plt.scatter(n, y3, label='cos(w2n)+1')
plt.legend(loc='lower right')
plt.show()

plt.xlabel("n")
plt.ylabel("f(n)")
plt.title('plot for all')
plt.scatter(n, y1, label='cos(w0n)')
plt.scatter(n, y2, label='cos(w1n)+0.5')
plt.scatter(n, y3, label='cos(w2n)+1')
plt.legend(loc='lower right')
plt.show()
