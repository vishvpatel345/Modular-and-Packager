import math


def circle_area(r):
    return math.pi * r * r


def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)