# 1 == wall, 0 == open space
MAZE = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

START = (1, 1)  # MAZE [1][1]
GOAL = (5, 5)


def print_maze(maze):
    for row_index, row in enumerate(maze):
        for column_index, cell in enumerate(row):
            position = (row_index, column_index)

            if position == START:
                print("S", end=" ")
            elif position == GOAL:
                print("G", end=" ")
            elif cell == 1:
                print("█", end=" ")
            else:
                print(" ", end=" ")

        print()


if __name__ == "__main__":
    print_maze(MAZE)
