import random
from generated_maze import create_maze, print_maze


if __name__ == "__main__":
    # Generate and print the maze
    maze_grid = create_maze(width=39, height=19)
    print_maze(maze_grid)
