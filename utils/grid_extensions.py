def get_neighbors(coordinate, grid, cardinal):

    if cardinal:
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    else:
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]


    neighbors = [(coordinate[0] + dr, coordinate[1] + dc) for dr, dc in directions]
    valid_coordinates = [neighbor for neighbor in neighbors if neighbor in grid]
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


def show(grid):
    max_i = max([pos[0] for pos in grid.keys()])
    max_j = max([pos[1] for pos in grid.keys()])

    pic = [[None for h in range(max_j+1)] for w in range(max_i+1)]

    for i, row in enumerate(pic):
        for j, _ in enumerate(row):
            pic[i][j] = grid[(i, j)]

    for line in pic:
        print(''.join(line))
    print()
