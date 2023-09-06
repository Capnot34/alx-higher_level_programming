#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, n, solutions):
    """Utilizes backtracking to find all solutions."""
    if col >= n:
        solutions.append([''.join(['Q' if c else '.' for c in row]) for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n, solutions)
            board[i][col] = 0  # backtrack

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_nqueens(board, 0, n, solutions)

    for solution in solutions:
        formatted_solution = []
        for i, row in enumerate(solution):
            for j, char in enumerate(row):
                if char == 'Q':
                    formatted_solution.append([i, j])
        print(formatted_solution)
