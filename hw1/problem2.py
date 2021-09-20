import numpy as np


def num_exp(x, n):
    x = np.array(x, dtype=np.float64)
    if n == 0:
        return 1
    tmp = 1
    for i in range(n):
        tmp += (x ** (i + 1)) / np.math.factorial(i + 1)
    return tmp

