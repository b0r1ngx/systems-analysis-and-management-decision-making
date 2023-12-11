from scipy.optimize import minimize

from nonlinear.constants import start_point
from nonlinear.unconstraints.plotting import plot
from nonlinear.save_step import save_step, steps
from nonlinear.task import f, gradient

sor = 'SLSQP'
result = minimize(
    fun=f,
    x0=start_point,
    method=sor,
    jac=gradient,
    callback=save_step
)
print(result)
print(steps)
plot(steps)