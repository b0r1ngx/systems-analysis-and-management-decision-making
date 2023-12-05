import numpy as np
from scipy.optimize import minimize

from datalayer.Point import Point


def _f(point: Point):
    x1 = point.x
    x2 = point.y
    return -4 * x1 * x1 - 4 * x2 * x2 + 4 * x1 * x2 + 8 * x1 + 20 * x2


# todo: find it automatically?
def _gradient(point: Point):
    x1 = point.x
    x2 = point.y
    return np.array([
        -8 * x1 + 4 * x2 + 8,
        -8 * x2 + 4 * x1 + 20
    ])


def f(x):
    x1 = x[0]
    x2 = x[1]
    return -(-4 * x1 * x1 - 4 * x2 * x2 + 4 * x1 * x2 + 8 * x1 + 20 * x2)


def gradient(x):
    x1 = x[0]
    x2 = x[1]
    return np.array([
        -(-8 * x1 + 4 * x2 + 8),
        -(-8 * x2 + 4 * x1 + 20)
    ])


result = minimize(
    f, np.zeros(2),
    method='trust-constr',
    jac=gradient
)

print(result)
print(result.x)
result = -f(result.x)
print(result)

my_result = _f(Point(3, 4))
print(my_result)
