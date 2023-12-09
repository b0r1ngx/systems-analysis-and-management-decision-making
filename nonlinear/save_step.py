import numpy

steps = []


def save_step(*args):
    for arg in args:
        if type(arg) is numpy.ndarray:
            steps.append(arg)
