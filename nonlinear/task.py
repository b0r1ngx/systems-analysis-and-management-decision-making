import numpy as np


def f(x):
    x1, x2 = x[0], x[1]
    return -(-4 * x1 * x1 - 4 * x2 * x2 + 4 * x1 * x2 + 8 * x1 + 20 * x2)


# first derivative of f for each variable
# f' by x1, f' by x2
def gradient(x):
    x1, x2 = x[0], x[1]
    return np.array([
        -(-8 * x1 + 4 * x2 + 8),
        -(-8 * x2 + 4 * x1 + 20)
    ])