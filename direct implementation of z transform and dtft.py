import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
import math as m


def dtft(x, N):
    xw = []
    j = cm.sqrt(-1)
    n = len(x)
    w = np.linspace(0, 2 * np.pi, N)
    for i in range(0, N):
        sum = 0
        w_temp = w[i]
        for k in range(0, n):
            sum = (sum + (x[k] * np.exp((-j) * w_temp * k)))
        xw.append(sum)
    return (xw)


def zfunc(z):
    return ((z**4 + z**3 + z**2 + z + 1)/(z**4)) #direct from F(z)


j = cm.sqrt(-1)
start = 0
finish = 100
shape = finish - start
n = np.linspace(0,2*np.pi,shape)
#n = np.arange(start, finish, 1) #if this is done with linspace it wont allow me to use the scipy built in impulse function there for i use arange
#signal for part b,
fnb = signal.unit_impulse(shape, 0) + \
     signal.unit_impulse(shape, 0 + 1) + \
     signal.unit_impulse(shape, 0 + 2) + \
     signal.unit_impulse(shape, 0 + 3) + \
     signal.unit_impulse(shape, 0 + 4)

n2 = np.linspace(0,2*np.pi, shape)

fnd = signal.unit_impulse(shape, 0) + \
     signal.unit_impulse(shape, 0 + 1) + \
     signal.unit_impulse(shape, 0 + 2) + \
     signal.unit_impulse(shape, 0 + 3) + \
     signal.unit_impulse(shape, 0 + 4)

#############################################seif 2###################################################
fz = dtft(fnb, len(n))
print(fz)
#print(np.fft.fftshift(abs(np.real(fz))))

plt.plot(n, np.fft.fftshift(abs(np.real(fz))))
plt.show()
######################################################################################################

#######################################seif 3########################################################
z = zfunc(np.exp(-j*n2))
#z = dtft(z, shape)
#print(z)
#print(abs(np.fft.fftshift(z)))

plt.plot(n2, abs(np.fft.fftshift(z)))
plt.show()
######################################################################################################

######################seif 4###################################
plt.stem(n2, np.fft.fftshift(abs(np.fft.fft(fnd))))
plt.show()
##############################################################