#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda l: list(map(lambda m: m**2, l)), matrix)))
