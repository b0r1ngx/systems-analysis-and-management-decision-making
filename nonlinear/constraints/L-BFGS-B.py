from scipy.optimize import minimize

from nonlinear.constants import start_point
from nonlinear.constraints.constraints import (
    bounds, constraints, eq_constraints, radial_constraints, radial_bounds)
from nonlinear.unconstraints.plotting import plot, plot_with_constraints
from nonlinear.save_step import save_step, steps
from nonlinear.task import f, gradient

constraints = constraints
bounds = bounds
result = minimize(
    fun=f,
    x0=start_point,
    method='L-BFGS-B',
    jac=gradient,
    bounds=bounds,
    constraints=constraints,
    callback=save_step
)
print(result)
print(steps)
plot_with_constraints(steps, constraints)
