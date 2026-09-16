import random

from maze import GOAL, MAZE, START

POPULATION_SIZE = 100  # 100 solutions
GENOME_LENGTH = 9  # Length of individual solution
MUTATION_RATE = 0.01  # Probability of mutation happening
CROSSOVER_RATE = 0.7  # How likely will the parents will mate / reproduce
GENERATIONS = 100  # How many times the process will be repeated

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


# Select parent function -> algorithm to pick the parents
def select_parent(population, fitness_values):
    total_fitness = sum(fitness_values)
    # randomly pick value between 0 and the total_fitness
    pick = random.uniform(0, total_fitness)
    current = 0
    # for each individual in population and corresponding fitness score, zip (combine 2 variables)
    for individual, fitness_value in zip(population, fitness_values):
        # increase current value by fitness score
        current += fitness_value
        # if current value becomes larger than or equal to the random pick, return the individual (parent)
        if current >= pick:
            return individual


# Reproduction function -> pick 1st half of parent #1 and 2nd half parent #2
def crossover(parent1, parent2):
    # if random point is less than the crossover rate, return crossovers
    if random.random() < CROSSOVER_RATE:
        # Crossover point is a random point between the length of the parents
        crossover_point = random.randint(1, len(parent1) - 1)
        # Crossover / Reproduction between parents
        return (
            parent1[:crossover_point] + parent2[crossover_point:],
            parent2[:crossover_point] + parent1[crossover_point:],
        )
    # else return the parents
    else:
        return parent1, parent2


# Mutation function -> mutating the genome
def mutate(genome):
    # for each bit within the genome
    for i in range(len(genome)):
        # for each bit, there is a 1% chance (mutation rate) that the genes are changed inside an individual genome
        if random.random() < MUTATION_RATE:
            # if the 1% chance happens, mutation occurs within individual genome
            genome[i] = random.choice(possible_moves)

    # return genome once done with mutation
    return genome


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


# Genetic Algorithm function
def genetic_algorithm():
    population = init_population(POPULATION_SIZE, GENOME_LENGTH)

    # Run generations with genetic algorithm of crossover and mutation
    for generation in range(GENERATIONS):
        # Calculate all of the fitness values for each genome in the population
        fitness_values = [
            fitness(move_agent(MAZE, START, genome)) for genome in population
        ]

        # Define new population of next generation
        new_population = []
        # For the population (divide by 2 since we always take 2 parents)
        for _ in range(POPULATION_SIZE // 2):
            # Select 2 parents
            parent1 = select_parent(population, fitness_values)
            parent2 = select_parent(population, fitness_values)
            # Generate offspring
            offspring1, offspring2 = crossover(parent1, parent2)
            # Mutate the offsprings and extend them to the new population
            new_population.extend([mutate(offspring1), mutate(offspring2)])

        # Redeclare the original population as the new population with the mutated offsprings
        population = new_population

        # Get all the fitness values
        fitness_values = [
            fitness(move_agent(MAZE, START, genome)) for genome in population
        ]
        # Declare best fitness value as the max of the fitness values
        best_fitness = max(fitness_values)
        # Print status message to show best fitness value for each generation
        print(f"Generation {generation}: Best Fitness = {best_fitness}")

    # After the generations run, the best index is the max of the fitness values
    best_index = fitness_values.index(max(fitness_values))
    # Declare best solution as the individual genome with the best index (fitness value)
    best_solution = population[best_index]
    # Prints best solution to problem
    print(f"Best Solution: {best_solution}")
    # Prints the fitness value of the best solution
    print(f"Best Fitness: {fitness(move_agent(MAZE, START, best_solution))}")


if __name__ == "__main__":
    genetic_algorithm()
