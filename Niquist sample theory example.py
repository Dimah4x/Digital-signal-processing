import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
import math as m

################seif a+b#############################
f = 1000
T = 1 / f
cycles = 100
points = 100
length = T * cycles
continuous = cycles * points
n = np.linspace(0, (continuous - 1) * length / continuous, continuous)
sinea = np.sin(2 * np.pi * f * n)
print(length)
plt.plot(n, sinea)
plt.show()

#seif c+d

f = 4000
T = 1 / f
cycles = 100
points = 100
length = 4 * T * cycles
continuous = cycles * points
n = np.linspace(0, ((continuous - 1) / continuous) * length, continuous)
sine = np.sin(2 * np.pi * f * n)
print('since the frequency quadrupled the time for each sample was divided by 4 therefor the amount of sampling points went up by 4')
plt.plot(n,sine)
plt.show()

#for i in range(f):
    #sine2 = np.sin(2 * np.pi*f)
    #plt.stem(T, sine2)

#plt.show()


n1 = np.linspace(-((((continuous)-1)/2) / continuous) * f, ((((continuous) -1)/2) / continuous) * f, continuous)
sine = np.sin(2 * np.pi * f * n)
plt.stem(n1, abs(np.fft.fftshift(np.fft.fft(sine))))
plt.show()
