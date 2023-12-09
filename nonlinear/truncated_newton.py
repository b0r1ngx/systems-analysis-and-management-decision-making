from scipy.optimize import minimize, OptimizeResult

from nonlinear.constants import start_point
from nonlinear.save_step import save_step, steps
from nonlinear.task import f, gradient

truncated_newton = 'Newton-CG'
result: OptimizeResult = minimize(
    fun=f,
    x0=start_point,
    method=truncated_newton,
    jac=gradient,
    callback=save_step
)
print(result)
print(steps)
