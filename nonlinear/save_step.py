import numpy

from nonlinear.constants import start_point

steps = [start_point]


def save_step(*args):
    for arg in args:
        if type(arg) is numpy.ndarray:
            steps.append(arg)
