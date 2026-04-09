# astar.py — A* Path Planning Algorithm

import heapq

def heuristic(a, b):
    """Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal, rows, cols):
    """
    A* algorithm.
    Returns: (path as list of (row,col) tuples, visited set)
    Returns (None, visited) if no path exists.
    """
    from src.grid import get_neighbors

    # Priority queue: (f_score, node)
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}          # tracks the path
    g_score = {start: 0}   # cost from start to node
    f_score = {start: heuristic(start, goal)}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        # Goal reached — reconstruct path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, visited

        for neighbor in get_neighbors(current, grid, rows, cols):
            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, visited  # no path found