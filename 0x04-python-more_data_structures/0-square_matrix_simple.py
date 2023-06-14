#!/usr/bin/python3
def square_matrix_simple(matrix=None):
    """Compute the square value of all integers of a matrix."""
    if matrix is None:
        matrix = []

    if not matrix:
        return None

    return [[a**2 for a in row] for row in matrix]
