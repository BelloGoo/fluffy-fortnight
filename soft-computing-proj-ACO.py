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

# Define the ACO parameters
num_ants = 50
num_iterations = 100
evaporation_rate = 0.1
pheromone_deposit = 1.0
initial_pheromone = 0.1

# Initialize the pheromone matrix
num_positions = len(positions)
pheromone_matrix = [[initial_pheromone] * num_positions for _ in range(num_positions)]

# Perform ACO iterations
for _ in range(num_iterations):
    # Initialize ant solutions
    ant_solutions = [[] for _ in range(num_ants)]
    
    # Construct ant solutions
    for ant in range(num_ants):
        for _ in range(num_positions):
            # Select the next position based on the pheromone values and heuristic information
            current_position = ant_solutions[ant][-1] if ant_solutions[ant] else None
            remaining_positions = set(range(num_positions)) - set(ant_solutions[ant])
            
            if current_position is None:
                next_position = random.choice(list(remaining_positions))
            else:
                pheromone_values = [pheromone_matrix[current_position][position] for position in remaining_positions]
                heuristic_values = [1 / employee_costs[position] for position in remaining_positions]
                
                total = sum(pheromone_values[i] * heuristic_values[i] for i in range(len(remaining_positions)))
                probabilities = [pheromone_values[i] * heuristic_values[i] / total for i in range(len(remaining_positions))]
                
                next_position = random.choices(list(remaining_positions), probabilities)[0]
            
            ant_solutions[ant].append(next_position)
    
    # Update pheromone levels
    for i in range(num_positions):
        for j in range(num_positions):
            delta_pheromone = sum(pheromone_deposit / employee_costs[ant_solutions[ant][i]] for ant in range(num_ants) if ant_solutions[ant][i] == j)
            pheromone_matrix[i][j] = (1 - evaporation_rate) * pheromone_matrix[i][j] + delta_pheromone
    
# Find the best solution
best_solution = min(ant_solutions, key=lambda solution: sum(employee_costs[position-1] for position in solution))
minimum_total_cost = sum(employee_costs[position-1] for position in best_solution)

# Print the minimum total cost found by ACO
print("Minimum total cost:", minimum_total_cost)
