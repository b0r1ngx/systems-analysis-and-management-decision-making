from math import sqrt
from random import randint


def euclidean_dist(a: tuple[int], b: tuple[int]) -> float:
    """Calculates the Euclidean distance between two 2D points."""
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def calculate_dist(dm: list[list[float]], index: list[int]) -> float:
    """Calculates the path length based on the index list of the distance matrix."""
    dist = 0
    for i in range(len(index) - 1):
        dist += dm[index[i]][index[i + 1]]
    return dist


def distance_matrix(points: list[tuple[int, int]]) -> list[list[float]]:
    """Calculates the distance matrix for the given 2D points."""
    return [[euclidean_dist(a, b) for b in points] for a in points]


def generate_problem(count: int, canvas_size: int = 1000) -> list[tuple[int, int]]:
    return [(randint(0, canvas_size), randint(0, canvas_size)) for _ in range(count)]
