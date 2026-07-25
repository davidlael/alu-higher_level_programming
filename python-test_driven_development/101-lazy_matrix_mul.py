#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy

    Args:
        m_a: first matrix (list of lists)
        m_b: second matrix (list of lists)

    Returns:
        Result of matrix multiplication as numpy array
    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
