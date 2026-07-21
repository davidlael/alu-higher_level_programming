#!/usr/bin/python3
"""
Module 101-nqueens
Solves the N queens puzzle using backtracking.
"""
import sys


def print_usage_and_exit():
    """Prints usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def validate_args():
    """Validates command-line arguments."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_safe(board, row, col):
    """
    Checks if placing a queen at (row, col) is safe from attacks.

    Args:
        board (list): Current state of placed queens coordinates.
        row (int): Target row.
        col (int): Target column.

    Returns:
        bool: True if safe, False otherwise.
    """
    for q_row, q_col in board:
        if q_col == col or abs(q_row - row) == abs(q_col - col):
            return False
    return True


def solve_nqueens(n, row, board):
    """
    Recursively finds all solutions for the N queens problem.

    Args:
        n (int): Size of the board.
        row (int): Current row being evaluated.
        board (list): List storing placed queen positions [[r, c], ...].
    """
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(n, row + 1, board)
            board.pop()


def main():
    """Main execution function."""
    n = validate_args()
    solve_nqueens(n, 0, [])


if __name__ == "__main__":
    main()
