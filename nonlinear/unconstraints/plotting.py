import matplotlib.pyplot as pt
import numpy as np

from nonlinear.task import f


def plot(steps):
    fig = pt.figure()
    ax = fig.add_subplot(
        projection='3d'
    )

    xmesh, ymesh = np.mgrid[-1:5:50j, -1:5:50j]
    fmesh = f(np.array([xmesh, ymesh]))
    ax.plot_surface(xmesh, ymesh, fmesh)
    pt.show()

    pt.axis("equal")
    pt.contour(xmesh, ymesh, fmesh, 50)
    steps = np.array(steps)
    pt.plot(steps.T[0], steps.T[1], "x-")
    pt.show()
