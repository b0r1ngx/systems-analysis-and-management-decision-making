from scipy.optimize import minimize, OptimizeResult

from nonlinear.constants import start_point
from nonlinear.save_step import save_step, steps
from nonlinear.task import f, gradient

conjugate_gradient = 'CG'
result: OptimizeResult = minimize(
    fun=f,
    x0=start_point,
    method=conjugate_gradient,
    jac=gradient,
    callback=save_step
)
print(result)
print(steps)
