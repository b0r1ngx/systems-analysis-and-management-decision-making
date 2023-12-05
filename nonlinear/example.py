import numpy as np

from nonlinear.conjugate_gradient_method import fletcher_reeves


def rosenbrock(x):
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def rosenbrock_grad(x):
    return np.array([
        -400 * (x[1] - x[0] ** 2) * x[0] - 2 * (1 - x[0]),
        200 * (x[1] - x[0] ** 2)
    ])


x0 = np.array([0.5, 0.5])

res = fletcher_reeves(rosenbrock_grad, x0)

print("Minimum of Rosenbrock function:", res)

x = np.array([13, 37])

res = fletcher_reeves(rosenbrock_grad, x0)