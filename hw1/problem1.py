import numpy as np


def derivative_forward(f, x, h):
    tmp = (f(x + h) - f(x)) / h
    return tmp


def derivative_centered(f, x, h):
    tmp = (f(x + h) - f(x - h)) / (2 * h)
    return tmp
