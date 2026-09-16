import random

from maze import GOAL, MAZE, START

POPULATION_SIZE = 100  # 100 solutions
GENOME_LENGTH = 20  # Length of individual solution
MUTATION_RATE = 0.01  # Probability of mutation happening
CROSSOVER_RATE = 0.7  # How likely will the parents will mate / reproduce
GENERATIONS = 200  # How many times the process will be repeated

genome = ["R", "L", "R", "U", "D", "R", "L", "D", "U", "D"]
possible_moves = ["R", "L", "U", "D"]


def random_genome(length):
    return random.choices(possible_moves, k=length)


def init_population(population_size, genome_length):
    genomes = []
    for _ in range(population_size):
        genomes.append(random_genome(genome_length))

    return genomes


def fitness(agent):
    distance = abs(GOAL[0] - agent[0]) + abs(GOAL[1] - agent[1])
    fitness_score = 1 / (distance + 1)

    return fitness_score


def move_agent(maze, start, genome):
    row, col = start
    for gene in genome:
        new_row, new_col = row, col

        if gene == "U":
            new_row -= 1
        elif gene == "D":
            new_row += 1
        elif gene == "L":
            new_col -= 1
        elif gene == "R":
            new_col += 1

        # Move only if new position is open
        if maze[new_row][new_col] == 0:
            row, col = new_row, new_col

    return (row, col)


if __name__ == "__main__":
    agent = move_agent(MAZE, START, genome)
    print(f"Agent Moves: {agent}")
    fitness_score = fitness(agent)
    print(f"Agent Fitness Score: {fitness_score}")
    initial_population = init_population(POPULATION_SIZE, GENOME_LENGTH)
    print(f"Population Size: {len(initial_population)}")
    print(f"Genome: {initial_population[0]}")
