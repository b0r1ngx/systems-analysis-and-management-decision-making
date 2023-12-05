import matplotlib.pyplot as pt
import numpy as np
import scipy.optimize as sopt
from scipy.spatial import distance

from nonlinear.steepest_descent.steepest_descent import gradient, f

fig = pt.figure()
ax = fig.add_subplot(projection='3d')

xmesh, ymesh = np.mgrid[0:6:50j, 1:7:50j]
fmesh = f(np.array([xmesh, ymesh]))
ax.plot_surface(xmesh, ymesh, fmesh)
pt.show()

guesses = [np.array([2, 2])]
tol = .1
while True:
    x = guesses[-1]
    s = -gradient(x)


    def f1d(alpha):
        return f(x + alpha * s)


    alpha_opt = sopt.golden(f1d)
    next_guess = x + alpha_opt * s
    guesses.append(next_guess)
    print('guesses:', guesses)
    print('next guess:', next_guess)
    diff = distance.euclidean(guesses[-2], guesses[-1])
    if diff < tol:
        break

pt.axis("equal")
pt.contour(xmesh, ymesh, fmesh, 50)
it_array = np.array(guesses)
pt.plot(it_array.T[0], it_array.T[1], "x-")
pt.show()
