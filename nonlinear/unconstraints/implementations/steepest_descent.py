import numpy as np

from nonlinear.constants import start_point
from nonlinear.unconstraints.plotting import plot
from nonlinear.save_step import save_step, steps
from nonlinear.task import gradient


def steepest_descent(
        x0, learning_rate=.1,
        max_iterations=1000,
        eps=1e-8, callback=None
):
    x = x0
    i = 0
    grad = gradient(x)

    while i < max_iterations and np.linalg.norm(grad, ord=np.inf) > eps:
        grad = gradient(x)
        x = x - learning_rate * grad
        callback(x)
        i += 1
    return x


result = steepest_descent(
    start_point,
    callback=save_step
)
print(result)
print(steps)
print(steps[20])
print(len(steps))
plot(steps)
