from scipy.optimize import minimize

from nonlinear.constants import start_point
from nonlinear.constraints.constraints import (
    bounds, eq_bounds, radial_bounds,
    constraints, eq_constraints, radial_constraints)
from nonlinear.unconstraints.plotting import plot, plot_with_constraints
from nonlinear.save_step import save_step, steps
from nonlinear.task import f, gradient

constraints = eq_constraints
bounds = eq_bounds
result = minimize(
    fun=f,
    x0=start_point,
    method='trust-constr',
    jac=gradient,
    # bounds=bounds,
    constraints=constraints,
    callback=save_step
)
print(result)
print(steps)
plot_with_constraints(steps, constraints)
