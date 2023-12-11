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


# to use 1, 2, 3, 4 constraints, use constraints + bounds
constraints = (
    {'type': 'ineq', 'fun': first},
    {'type': 'ineq', 'fun': second},
    # {'type': 'ineq', 'fun': third},  ||
    # {'type': 'ineq', 'fun': fourth}, ||
)  # third & fourth goes to bounds     VV
bounds = ((0, None), (0, None))

eq_constraints = (
    {'type': 'eq', 'fun': fifth}
)

radial_constraints = (
    {'type': 'ineq', 'fun': sixth},
    {'type': 'ineq', 'fun': seventh},
)