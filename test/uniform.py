from random import random, uniform

random = random()


# if we need a random number between [a, b]
def first(a, b):
    return (b - a) + a * (2 * random - 1)


# random.uniform(a, b) == return a + (b - a) * self.random()
# check realisation of random.uniform()
def second(a, b):
    return a + (b - a) * random


if __name__ == '__main__':
    a, b = 3, 9
    assert first(a, b) == second(a, b)
