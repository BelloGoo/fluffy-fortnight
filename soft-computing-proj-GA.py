import random

# Define the positions and their suitable employees
positions = {
    'Masonry': [1, 9, 19, 22, 25, 28, 31],
    'Carpentry': [2, 12, 15, 19, 21, 23, 27, 29, 30, 31, 32],
    'Plumbing': [3, 10, 19, 24, 26, 30, 32],
    'Ceiling': [4, 21, 25, 28, 32],
    'Electricity': [5, 11, 16, 22, 23, 27, 31],
    'Heating': [6, 20, 24, 26, 30, 32],
    'Insulation': [7, 12, 17, 25, 30, 31],
    'Roofing': [8, 17, 20, 22, 23],
    'Painting': [9, 13, 14, 26, 29, 30, 31],
    'Windows': [10, 21, 25, 31, 32],
    'Facade': [14, 15, 18, 23, 24, 27, 30, 32],
    'Garden': [18, 19, 22, 24, 26, 29, 31],
    'Garage': [11, 20, 25, 28, 30, 32],
    'Driveway': [16, 19, 23, 31],
    'Moving': [9, 18, 26, 28, 31, 32]
}

# Define the cost of each employee
employee_costs = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 9]

# Define the GA parameters
population_size = 100
max_generations = 100
mutation_rate = 0.1

# Define the fitness function to minimize the total cost
def fitness_function(positions, individual):
    total_cost = 0
    for position, employees in positions.items():
        assigned_employees = [employee for idx, employee in enumerate(individual) if idx + 1 in employees]
        if len(assigned_employees) == 0:
            total_cost += min(employee_costs)
        else:
            total_cost += sum([employee_costs[emp - 1] for emp in assigned_employees])
    return total_cost

# Initialize the population randomly
population = [[random.randint(1, 32) for _ in range(len(positions))] for _ in range(population_size)]

# Perform GA iterations
for generation in range(max_generations):
    # Calculate the fitness of each individual in the population
    fitness_values = [fitness_function(positions, individual) for individual in population]
    
    # Select parents for mating (tournament selection)
    selected_parents = []
    for _ in range(population_size):
        tournament_size = 5
        participants = random.sample(range(population_size), tournament_size)
        selected_parent = min(participants, key=lambda x: fitness_values[x])
        selected_parents.append(population[selected_parent])
    
    # Perform crossover to create the offspring
    offspring = []
    for i in range(0, population_size, 2):
        parent1 = selected_parents[i]
        parent2 = selected_parents[i+1]
        crossover_point = random.randint(1, len(positions)-1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        offspring.append(child1)
        offspring.append(child2)
    
    # Perform mutation on the offspring
    for i in range(population_size):
        if random.random() < mutation_rate:
            mutation_point = random.randint(0, len(positions)-1)
            offspring[i][mutation_point] = random.randint(1, 32)
    
    # Replace the old population with the offspring
    population = offspring
    
# Calculate the fitness of the final population
fitness_values = [fitness_function(positions, individual) for individual in population]

# Find the best individual with the minimum total cost
best_individual = population[fitness_values.index(min(fitness_values))]
minimum_total_cost = min(fitness_values)

# Print the minimum total cost found by GA
print("Minimum total cost:", minimum_total_cost)
