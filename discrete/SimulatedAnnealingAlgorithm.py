from numpy import exp
from random import sample, random

from datalayer.Path import Path
from discrete.utils import *


class SimulatedAnnealingAlgorithm:
    """
    Simulated annealing is a probabilistic technique for approximating the global optimum of a given function.
    Specifically, it is a metaheuristic to approximate global optimization in a large search space for an optimization problem.
    -----
    `iter: int` THE NUMBER OF ITERATIONS
    The maximum number of iterations of the algorithm.
    -----
    `t: int` INITIAL TEMPERATURE
    The initial temperature for the search decreases with the progress of the search.
    -----
    `g: float` CHANGE COEFFICIENT
    The coefficient affecting temperature change.
    """

    def __init__(self, iter: int, t: int, g: float) -> None:
        """Initializes the hyperparameters for the algorithm."""
        self.iter = iter
        self.t = t
        self.g = g

    def __is_acceptable(self, prb_length: float, tmp_leng: float) -> bool:
        """Checks if the state transition will execute."""
        prob = min(1, exp(-(prb_length - tmp_leng) / self.t))
        if prob > random():
            return True
        return False

    def run(self, points: list[tuple[int, int]]) -> Path:
        """Runs the algorithm for the given 2D points."""
        l = len(points)
        dm = distance_matrix(points)
        tmp_index = [i for i in range(l)] + [0]
        tmp_length = calculate_dist(dm, tmp_index)
        res_index = tmp_index.copy()
        res_length = tmp_length
        for _ in range(self.iter):
            i, j = sample(range(1, l), 2)
            prb_index = tmp_index.copy()
            prb_index[i], prb_index[j] = prb_index[j], prb_index[i]
            prb_length = calculate_dist(dm, prb_index)

            if self.__is_acceptable(prb_length, tmp_length):
                tmp_index = prb_index
                tmp_length = prb_length

            if tmp_length < res_length:
                res_index = tmp_index
                res_length = tmp_length

            self.t *= self.g

        return Path(
            indices=res_index,
            length=res_length,
            name="Simulated Annealing Algorithm"
        )
