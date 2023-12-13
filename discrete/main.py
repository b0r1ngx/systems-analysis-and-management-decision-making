from time import time

from discrete.utils import generate_problem
from discrete.GeneticAlgorithm import GeneticAlgorithm
from discrete.SimulatedAnnealingAlgorithm import SimulatedAnnealingAlgorithm
from discrete.AntColonyOptimization import AntColonyOptimization
from discrete.TravellingSalesmanProblem import TravellingSalesmanProblem


def main() -> None:
    points = generate_problem(20)
    paths = []

    _time = time()
    aco = AntColonyOptimization(
        ants=100, iter=20, a=1.5, b=1.2, p=0.6, q=10
    )
    paths.append(aco.run(points=points))
    print(f"ACO time: {time() - _time}")

    _time = time()
    ga = GeneticAlgorithm(
        population=1500, iter=40, s=0.2, m=0.5
    )
    paths.append(ga.run(points=points))
    print(f"GeneticAlgorithm work time: {time() - _time}")

    _time = time()
    sa = SimulatedAnnealingAlgorithm(
        iter=20000, t=100, g=0.6
    )
    paths.append(sa.run(points=points))
    print(f"SA time: {time() - _time}")

    TravellingSalesmanProblem(points=points, paths=paths)


if __name__ == "__main__":
    main()
