# grid.py — Creates the simulation grid with obstacles

import numpy as np
import random

def create_grid(rows, cols, obstacle_density, seed=42):
    """
    Creates a 2D grid where:
      0 = free cell
      1 = obstacle
    """
    random.seed(seed)
    grid = np.zeros((rows, cols), dtype=int)

    for r in range(rows):
        for c in range(cols):
            if random.random() < obstacle_density:
                grid[r][c] = 1  # place obstacle

    return grid

def place_start_goal(grid, rows, cols):
    """
    Places start (top-left area) and goal (bottom-right area).
    Ensures they are always on free cells.
    """
    # Force start and goal to be free
    start = (0, 0)
    goal  = (rows - 1, cols - 1)

    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]]   = 0

    return start, goal

def get_neighbors(node, grid, rows, cols):
    """
    Returns valid neighboring cells (up, down, left, right).
    """
    r, c = node
    neighbors = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == 0:  # only free cells
                neighbors.append((nr, nc))
    return neighbors