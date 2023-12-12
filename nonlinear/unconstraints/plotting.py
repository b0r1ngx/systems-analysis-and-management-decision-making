import matplotlib.pyplot as pt
import numpy as np
from scipy.optimize import NonlinearConstraint

from nonlinear.task import f


def plot(
        steps, with_3d=False,
        merge_solve_n_constraints=False
):
    fig = pt.figure()
    ax = fig.add_subplot(
        projection='3d'
    )

    x = np.linspace(-1, 10, 1000)
    x, y = np.meshgrid(x, x)
    fmesh = f(np.array([x, y]))
    if with_3d:
        ax.plot_surface(x, y, fmesh)
        pt.show()

    # pt.axis("equal")
    pt.contour(x, y, fmesh, 50)
    steps = np.array(steps)
    pt.plot(steps.T[0], steps.T[1], "x-")
    if not merge_solve_n_constraints:
        pt.show()


def plot_with_constraints(
        steps,
        constraints: tuple[NonlinearConstraint],
        with_3d=False,
        merge_solve_n_constraints=True
):
    # plot(steps, with_3d, merge_solve_n_constraints)
    plot_coord_from, plot_coord_to = -40, 40
    x = np.linspace(
        plot_coord_from, plot_coord_to,
        1000
    )
    x, y = np.meshgrid(x, x)

    fig = pt.figure()
    ax = fig.add_subplot(
        projection='3d'
    )
    fmesh = f(np.array([x, y]))
    ax.plot_surface(x, y, fmesh)
    pt.show()

    to_plot = 1
    for constraint in constraints:
        to_plot &= constraint.fun((x, y)) <= 0

    # plot the lines defining the constraints
    # x1, x2 >= 0
    y1 = x * 0
    # x2 <= (36 - 9 * x1) / 4
    y2 = (36 - 9 * x) / 4.0
    # x2 <= 6 - x
    y3 = 6 - x

    # color region of constraints
    pt.imshow(
        to_plot,
        extent=(x.min(), x.max(), y.min(), y.max()),
        origin="lower",
        cmap="Greys",
        alpha=0.3
    )

    steps = np.array(steps)
    pt.plot(steps.T[0], steps.T[1], "x-")
    pt.plot(0, "x-", label='x1 >= 0')
    pt.plot(x, y1, color='green', label='x2 >= 0')
    pt.plot(x, y2, label='9*x1 + 4*x2 <= 36')
    pt.plot(x, y3, label='x1 + x2 <= 6')
    pt.xlim(-5, plot_coord_to)
    pt.ylim(-5, plot_coord_to)
    pt.xlabel('x1')
    pt.ylabel('x2')

    # pt.legend()
    pt.show()
