import matplotlib.pyplot as plt
import numpy as np
import math
# this is 1 and 2


def unit_step(a, n): #define unit step function
    unit = []
    for sample in n:
        if sample < a:
            unit.append(0)
        else:
            unit.append(1)
    return unit


def linear_conv_matrix(x1, x2, diff):
    if len(x1) > len(x2):  # check size
        x2 = np.pad(x2, (0, len(x1) - len(x2)), mode='constant')
    elif len(x2) > len(x1):
        x1 = np.pad(x1, (0, len(x2) - len(x1)), mode='constant')
    print(diff)
    rows, columns = (len(x1), len(x2))
    length = rows + columns - 1
    extend_rows = length - rows
    extend_columns = length - columns
    yn = [[0 for x in range(rows)] for y in range(columns)]
    for i in range(rows):
        for j in range(columns):
            yn[i][j] = x1[i] * x2[j]
    yn = np.pad(yn, ((0, extend_rows), (0, extend_columns)), mode='constant')
    for length in yn:  # this line does nothing but the code doesn't work without it
        break
    # shift rows
    for x in range(len(length)):
        tmp = yn[x]
        tmp = np.roll(tmp, x)
        yn[x] = tmp
    print(yn)
    # sum columns
    zn = [0 for x in range(len(length)-diff)]
    for x in range(len(length)-diff):
        for y in range(len(length)-diff):
            zn[x] += yn[y][x]
    print(zn)
    return zn


start = -20
finish = 20
n = np.arange(start, finish, 1)
unit1 = unit_step(a=0,n=n)
unit2 = unit_step(a=5,n=n)
x1 = [unit1-unit2 for unit1,unit2 in zip(unit1,unit2)]
x2 = [1 for x in range(5)]
conv_len = math.ceil((len(x1) + len(x2))/2) * 2
diff = abs(len(x1) - len(x2))
print(diff)
y = linear_conv_matrix(x1, x2, diff)
y = y[abs(start):finish-start]
y = np.pad(y, (abs(start), 0), mode='constant')
print(y)
plt.stem(n, y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.xticks(n)
plt.title('y[n]')
plt.show()
