from scipy.optimize import golden
from scipy.spatial import distance

from nonlinear.constants import start_point
from nonlinear.unconstraints.plotting import plot
from nonlinear.task import gradient, f

guesses = [start_point, ]
tol = .01
niter = 0
while True:
    x = guesses[-1]
    s = -gradient(x)


    def f1d(alpha):
        return f(x + alpha * s)


    alpha_opt = golden(f1d)
    next_guess = x + alpha_opt * s
    guesses.append(next_guess)
    diff = distance.euclidean(
        guesses[-2], guesses[-1]
    )
    niter += 1
    if diff < tol:
        break

print(niter)
print(guesses)
plot(guesses)
