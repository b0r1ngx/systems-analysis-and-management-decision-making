from scipy.optimize import minimize

from nonlinear.constants import start_point
from nonlinear.constraints.constraints import (
    bounds, constraints, eq_constraints, radial_constraints)
from nonlinear.unconstraints.plotting import plot, plot_with_constraints
from nonlinear.save_step import save_step, steps
from nonlinear.task import f, gradient



# For equality constrained problems it is an implementation of Byrd-Omojokun
#     Trust-Region SQP method described in [17]_ and in [5]_, p. 549. When
#     inequality constraints are imposed as well, it swiches to the trust-region
#     interior point method described in [16]_. This interior point algorithm,
#     in turn, solves inequality constraints by introducing slack variables
#     and solving a sequence of equality-constrained barrier problems
#     for progressively smaller values of the barrier parameter.
#     The previously described equality constrained SQP method is
#     used to solve the subproblems with increasing levels of accuracy
#     as the iterate gets closer to a solution.
result = minimize(
    fun=f,
    x0=start_point,
    method='trust-constr',
    jac=gradient,
    # bounds=bounds,
    constraints=eq_constraints,
    callback=save_step
)
print(result)
print(steps)
plot_with_constraints(steps, eq_constraints)
