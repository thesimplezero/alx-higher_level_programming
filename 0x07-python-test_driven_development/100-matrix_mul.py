#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a, m_b: matrices to be multiplied (lists of lists of ints/floats).

    Raises:
        TypeError: If m_a or m_b is not a list of lists of ints/floats.
        TypeError: If m_a or m_b has different-sized rows or is empty.
        ValueError: If m_a and m_b cannot be multiplied.

    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    err1 = " must be a list of lists"
    if not isinstance(m_a, list) or not all(isinstance(r, list) and r for r in m_a):
        raise TypeError("m_a" + err1)
    if not isinstance(m_b, list) or not all(isinstance(r, list) and r for r in m_b):
        raise TypeError("m_b" + err1)

    err2 = " should contain only integers or floats"
    if not all((isinstance(e, int) or isinstance(e, float))
               for e in [n for r in m_a for n in r]):
        raise TypeError("m_a" + err2)
    if not all((isinstance(e, int) or isinstance(e, float))
               for e in [n for r in m_b for n in r]):
        raise TypeError("m_b" + err2)

    err3 = "each row of must be of the same size"
    if not all(len(r) == len(m_a[0]) for r in m_a):
        raise TypeError("m_a: " + err3)
    if not all(len(r) == len(m_b[0]) for r in m_b):
        raise TypeError("m_b: " + err3)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[sum(a * b for a, b in zip(r_a, c_b))
            for c_b in zip(*m_b)] for r_a in m_a]
    
    return res
