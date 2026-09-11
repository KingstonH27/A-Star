import grid


def run():
    # Write your pathfinding algorithm here
    # grid.gridData[row][col] gives you the tile

    # Example:
    start = (0, 0)
    end = (10, 10)

    # YOUR ALGORITHM GOES HERE



def get_neighbors(row, col):
    """Get the 4 adjacent tiles."""
    neighbors = []

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    for dr, dc in directions:
        r = row + dr
        c = col + dc

        if 0 <= r < len(grid.gridData) and 0 <= c < len(grid.gridData[0]):
            if grid.gridData[r][c] == 0:
                neighbors.append((r, c))

    return neighbors