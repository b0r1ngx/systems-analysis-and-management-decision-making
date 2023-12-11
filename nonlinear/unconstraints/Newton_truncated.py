from scipy.optimize import minimize, OptimizeResult

from nonlinear.unconstraints.plotting import plot
from nonlinear.task import f, gradient
from nonlinear.constants import start_point
from nonlinear.save_step import save_step, steps

Newton_truncated = 'Newton-CG'
result: OptimizeResult = minimize(
    fun=f,
    x0=start_point,
    method=Newton_truncated,
    jac=gradient,
    callback=save_step
)
print(result)
print(steps)
plot(steps)
