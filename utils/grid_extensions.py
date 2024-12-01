def get_neighbors(grid_size, x, y):
    coordinate = (x, y)

    # Neighbor directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    # Calculate neighbors
    neighbors = [(coordinate[0] + dr, coordinate[1] + dc) for dr, dc in directions]
    valid_coordinates = [(r, c) for r, c in neighbors if 0 <= r < grid_size and 0 <= c < grid_size]
    return valid_coordinates


def iterative_dfs(start, grid):
    """
    Perform an iterative DFS on a grid, visiting all reachable points.

    Args:
        start (tuple): Starting coordinate as (row, col).
        grid (list[list[int]]): The grid to traverse.

    Returns:
        set: A set of all visited nodes.
    """
    # Directions for neighbors (8 possible directions)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    rows, cols = len(grid), len(grid[0])
    visited = set()  # Track visited nodes
    stack = [start]  # Stack for DFS traversal

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        # Get neighbors
        neighbors = [
            (current[0] + dr, current[1] + dc)
            for dr, dc in directions
            if 0 <= current[0] + dr < rows and 0 <= current[1] + dc < cols
        ]

        # Add unvisited neighbors to the stack
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)

    return visited
