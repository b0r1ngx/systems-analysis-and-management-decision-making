import matplotlib.pyplot as pt
import numpy as np

from nonlinear.task import f


def plot(steps, with_3d=False):
    fig = pt.figure()
    ax = fig.add_subplot(
        projection='3d'
    )

    xmesh, ymesh = np.mgrid[-1:25:50j, -1:25:50j]
    fmesh = f(np.array([xmesh, ymesh]))
    if with_3d:
        ax.plot_surface(xmesh, ymesh, fmesh)
        pt.show()

    # pt.axis("equal")
    pt.contour(xmesh, ymesh, fmesh, 50)
    steps = np.array(steps)
    pt.plot(steps.T[0], steps.T[1], "x-")
    pt.show()


def plot_with_constraints(steps, constraints, with_3d=False):
    plot(steps, with_3d)
    # check this out: https://stackoverflow.com/questions/57017444/how-to-visualize-feasible-region-for-linear-programming-with-arbitrary-inequali
    for constraint in constraints:
        constraint

    d = np.linspace(-2, 16, 300)
    x, y = np.mgrid[-1:25:50j, -1:25:50j]  # np.meshgrid(d, d)
    pt.imshow(
        (y >= 2) & (2 * y <= 25 - x) & (4 * y >= 2 * x - 8) & (y <= 2 * x - 5),
        extent=(x.min(), x.max(), y.min(), y.max()), origin="lower", cmap="Greys", alpha=0.3
    )
    x = np.linspace(0, 16, 2000)
    # y >= 2
    # y1 = (x * 0) + 2
    # pt.plot(x, 2 * np.ones_like(y1))
    # pt.plot()
    pt.show()
