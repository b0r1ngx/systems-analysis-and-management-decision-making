import numpy as np


def fletcher_reeves(grad_f, x0, eps=1e-8, max_iter=1000):
    grad = grad_f(x0)
    p = - grad
    x = x0
    i = 0

    while i < max_iter and np.linalg.norm(grad, ord=np.inf) > eps:
        alpha = -(grad.dot(p)) / (p.dot(grad_f(p, x)))
        x = x + alpha * p
        old_grad = grad
        grad = grad_f(x)
        beta = (grad.dot(grad)) / (old_grad.dot(old_grad))
        p = -grad + beta * p
        i += 1

    return x
