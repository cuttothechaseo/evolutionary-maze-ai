import random

POPULATION_SIZE = 100  # 100 solutions
GENOME_LENGTH = 20  # Length of individual solution
MUTATION_RATE = 0.01  # Probability of mutation happening
CROSSOVER_RATE = 0.7  # How likely will the parents will mate / reproduce
GENERATIONS = 200  # How many times the process will be repeated


# Generating random list of 20 (GENOME_LENGTH) 0's and 1's
def random_genome(length):
    return [random.randint(0, 1) for _ in range(length)]


# Generating 100 random solutions (POPULATION_SIZE)
def init_population(population_size, genome_length):
    return [random_genome(genome_length) for _ in range(population_size)]


# Fitness function -> measuring the sum of the genome
def fitness(genome):
    return sum(genome)


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
        # if current value becomes larger than the random pick, return the individual (parent)
        if current > pick:
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
        # for each bit, there is a 1% chance (mutation rate) we are going to flip it
        if random.random() < MUTATION_RATE:
            # if the 1% chance happens, flip (mutate) the bit
            genome[i] = abs(genome[i] - 1)

        # return genome once done with mutation
        return genome


# Genetic Algorithm function
def genetic_algorithm():
    population = init_population(POPULATION_SIZE, GENOME_LENGTH)

    # Run generations with genetic algorithm of crossover and mutation
    for generation in range(GENERATIONS):
        # Calculate all of the fitness values for each genome in the population
        fitness_values = [fitness(genome) for genome in population]

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
        fitness_values = [fitness(genome) for genome in population]
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
    print(f"Best Fitness: {fitness(best_solution)}")


if __name__ == "__main__":
    genetic_algorithm()
