from random import random, shuffle
from math import inf

from datalayer.Path import Path
from discrete.utils import *


class AntColonyOptimization:
    """
    Ant Colony Optimization algorithm is introduced based on the foraging behavior of an ant
    for seeking a path between their colony and source food.
    -----
    `ants: int` THE NUMBER OF ANTS
    The total number of agents (ants) involved in one iteration.
    -----
    `iter: int` THE NUMBER OF ITERATIONS
    The maximum number of iterations of the algorithm.
    -----
    `a: float` INFORMATION ELICITATION FACTOR
    The information elicitation factor α, which represents the relative importance of the pheromone,
    reflects the importance of the accumulation of the pheromone with regard to the ants' path selection.
    -----
    `b: float` EXPECTED HEURISTIC FACTOR
    The expected heuristic factor β, which represents the relative importance of the visibility,
    reflects the importance of the heuristic information with regard to the ants' path selection.
    -----
    `p: float` PHEROMONE EVAPORATION COEFFICIENT
    The pheromone evaporation coefficient ρ, which represents the degree of pheromone evaporation,
    reflects the degree of mutual influence among ants. Generally, the value of  is [0, 1],
    which prevents the infinite accumulation of pheromone effectively.
    -----
    `q: float` PHEROMONE INTENSITY
    The pheromone intensity Q, which represents the total pheromone,
    affects the convergence speed of the alghoritm to a certain extent.
    """

    def __init__(self, ants: int, iter: int, a: float, b: float, p: float, q: float) -> None:
        """Initializes the hyperparameters for the algorithm."""
        self.ants = ants
        self.iter = iter
        self.a = a
        self.b = b
        self.p = p
        self.q = q

    @staticmethod
    def __select_i(selection: list[int]) -> int:
        """Selects a random index of the next 2D point."""
        sum_num = sum(selection)
        if sum_num == 0:
            return len(selection) - 1

        tmp_num = random()
        prob = 0
        for i in range(len(selection)):
            prob += selection[i] / sum_num
            if prob >= tmp_num:
                return i

    def __create_index(self, dm: list[list[float]], pm: list[list[float]]) -> list[int]:
        """Creates a new ordering of 2D point indices based on the distance and pheromone."""
        l = len(dm)
        unvisited_index = list(range(l))
        shuffle(unvisited_index)
        visited_index = [unvisited_index.pop()]
        for _ in range(l - 1):
            i = visited_index[-1]
            selection = []
            for j in unvisited_index:
                selection.append(
                    (pm[i][j] ** self.a) * ((1 / max(dm[i][j], 10 ** -5)) ** self.b)
                )
            selected_i = AntColonyOptimization.__select_i(selection)
            visited_index.append(unvisited_index.pop(selected_i))
        visited_index.append(visited_index[0])
        return visited_index

    def update_pm(self, pm: list[list[float]], tmp_index: list[list[int]], tmp_length: list[float]) -> None:
        """Updates the pheromone matrix."""
        l = len(pm)
        for i in range(l):
            for j in range(i, l):
                pm[i][j] *= 1 - self.p
                pm[j][i] *= 1 - self.p
        for i in range(self.ants):
            delta = self.q / tmp_length[i]

            index = tmp_index[i]
            for j in range(l):
                pm[index[j]][index[j + 1]] += delta
                pm[index[j + 1]][index[j]] += delta

    def run(self, points: list[tuple[int, int]]) -> Path:
        """Runs the algorithm for the given 2D points."""
        l = len(points)
        dm = distance_matrix(points)
        pm = [[1 for _ in range(l)] for _ in range(l)]
        res_index, res_length = [], inf
        for _ in range(self.iter):
            _index, _length = [], []
            for _ in range(self.ants):
                index = self.__create_index(dm, pm)
                _index.append(index)
                _length.append(calculate_dist(dm, index))

            self.update_pm(pm, _index, _length)
            best_length = min(_length)
            if best_length < res_length:
                res_length = best_length
                res_index = _index[_length.index(best_length)]

        return Path(
            indices=res_index,
            length=res_length,
            name="Ant Colony Optimization"
        )
