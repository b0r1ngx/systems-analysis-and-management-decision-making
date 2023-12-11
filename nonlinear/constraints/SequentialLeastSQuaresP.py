from scipy.optimize import minimize

from nonlinear.constants import start_point
from nonlinear.constraints.constraints import (
    bounds, constraints, eq_constraints, radial_constraints)
from nonlinear.unconstraints.plotting import plot
from nonlinear.save_step import save_step, steps
from nonlinear.task import f, gradient

result = minimize(
    fun=f,
    x0=start_point,
    method='SLSQP',
    jac=gradient,
    bounds=bounds,
    constraints=constraints,
    callback=save_step
)
print(result)
print(steps)
plot(steps)
