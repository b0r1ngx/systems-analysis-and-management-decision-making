from math import inf

from scipy.optimize import NonlinearConstraint


def first(x):
    x1, x2 = x[0], x[1]
    return 9 * x1 + 4 * x2 - 36  # <= 0


def second(x):
    x1, x2 = x[0], x[1]
    return x1 + x2 - 6  # <= 0


def third(x):
    x1 = x[0]
    return -x1  # <= 0


def fourth(x):
    x2 = x[1]
    return -x2  # <= 0


def fifth(x):
    x1, x2 = x[0], x[1]
    return x1 + x2 - 5  # == 0


def sixth(x):
    x1, x2 = x[0], x[1]
    return 4 * x1 * x1 + 9 * x2 * x2 - 144  # <= 0


def seventh(x):
    x1, x2 = x[0], x[1]
    return 9 * x1 * x1 + 25 * x2 * x2 - 225  # <= 0


# more than zero
inf_bounds = ((0, None), (0, None))
# to use 1, 2, 3, 4 constraints, use constraints + bounds
constraints = (
    NonlinearConstraint(fun=first, lb=-inf, ub=0),
    NonlinearConstraint(fun=second, lb=-inf, ub=0),
    # NonlinearConstraint(fun=third, lb=-inf, ub=0),
    # NonlinearConstraint(fun=fourth, lb=-inf, ub=0),
)  # third & fourth constraints goes to bounds V
bounds = ((0, 4), (0, 6))

eq_constraints = (
    {'type': 'eq', 'fun': fifth},
)
eq_bounds = ((4.99, 5.01), (4.99, 5.01))

radial_constraints = (
    NonlinearConstraint(fun=sixth, lb=-inf, ub=0),
    NonlinearConstraint(fun=seventh, lb=-inf, ub=0),
)
radial_bounds = ((-5, 5), (-3, 3))
