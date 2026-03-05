import random

cost_matrix = [
    [4, 6, 8, 7, 5],
    [7, 5, 6, 8, 4],
    [6, 4, 7, 5, 8],
    [5, 8, 6, 4, 7],
    [8, 6, 5, 7, 4],
    [7, 4, 8, 6, 5],
    [6, 7, 4, 5, 8],
    [5, 6, 7, 8, 4],
    [4, 7, 5, 6, 8],
    [8, 5, 6, 4, 7]
]

NUM_TASKS = 10
NUM_MACHINES = 5
GENERATIONS = 100
MUTATION_RATE = 0.1

def initialize_population(size):
    population = []
    for _ in range(size):
        chromosome = [random.randint(0, NUM_MACHINES-1) for _ in range(NUM_TASKS)]
        population.append(chromosome)
    return population

def total_cost(chromosome):
    return sum(cost_matrix[i][machine] for i, machine in enumerate(chromosome))

def fitness(chromosome):
    return 1 / total_cost(chromosome)

def selection(pop):
    pop_sorted = sorted(pop, key=lambda c: fitness(c), reverse=True)
    return pop_sorted[:len(pop)//2]

def crossover(parent1, parent2):
    point = random.randint(1, NUM_TASKS-2)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chromosome):
    for i in range(NUM_TASKS):
        if random.random() < MUTATION_RATE:
            chromosome[i] = random.randint(0, NUM_MACHINES-1)

def run_ga(pop_size):
    population = initialize_population(pop_size)
    best_solution = None
    best_fitness = 0
    best_gen = 0

    for gen in range(1, GENERATIONS+1):
        selected = selection(population)
        next_gen = []

        while len(next_gen) < pop_size:
            p1, p2 = random.sample(selected, 2)
            c1, c2 = crossover(p1, p2)
            mutate(c1)
            mutate(c2)
            next_gen.extend([c1, c2])

        population = next_gen[:pop_size]

        for chrom in population:
            f = fitness(chrom)
            if f > best_fitness:
                best_fitness = f
                best_solution = chrom
                best_gen = gen

    return best_solution, total_cost(best_solution), best_fitness, best_gen

for size in [10, 30]:
    solution, cost_val, fit_val, gen_val = run_ga(size)
    print(f"population size: {size}")
    print(f"best chromosome: {solution}")
    print(f"total cost: {cost_val}")
    print(f"fitness: {fit_val:.4f}")
    print(f"found in generation: {gen_val}\n")
