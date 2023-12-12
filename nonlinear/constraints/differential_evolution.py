from scipy.optimize import differential_evolution

from nonlinear.constants import start_point
from nonlinear.constraints.constraints import (
    bounds, eq_bounds, radial_bounds,
    constraints, eq_constraints, radial_constraints)
from nonlinear.unconstraints.plotting import plot, plot_with_constraints
from nonlinear.save_step import save_step, steps
from nonlinear.task import f, gradient

constraints = constraints
bounds = bounds
result = differential_evolution(
    func=f,
    bounds=bounds,
    x0=start_point,
    constraints=constraints,
    callback=save_step
)
print(result)
print(steps)
plot_with_constraints(steps, constraints)
