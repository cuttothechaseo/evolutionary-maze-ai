import random


def create_maze(width=39, height=19):
    # Ensure dimensions are odd numbers so walls align correctly
    if width % 2 == 0:
        width += 1
    if height % 2 == 0:
        height += 1

    # Initialize grid with walls (1)
    grid = [[1 for _ in range(width)] for _ in range(height)]

    # Iterative stack-based maze generation
    stack = [(1, 1)]
    grid[1][1] = 0

    while stack:
        cx, cy = stack[-1]
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)

        carved = False
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == 1:
                # Carve through the wall between cells
                grid[cy + dy // 2][cx + dx // 2] = 0
                grid[ny][nx] = 0
                stack.append((nx, ny))
                carved = True
                break

        if not carved:
            stack.pop()

    # Explicitly set entrance at top-left and exit at bottom-right
    grid[0][1] = 0
    grid[height - 2][width - 1] = 0

    return grid


def print_maze(grid):
    for row in grid:
        print("".join("  " if cell == 0 else "██" for cell in row))


if __name__ == "__main__":
    # Generate and print the maze
    maze_grid = create_maze(width=39, height=19)
    print_maze(maze_grid)
