#!/usr/bin/python3
"""Module for matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using NumPy.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        Product of m_a and m_b using numpy.matmul.
    """
    return np.matmul(m_a, m_b)
