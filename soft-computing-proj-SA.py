import random
import math

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

# Define the initial temperature and cooling rate
initial_temperature = 1000
cooling_rate = 0.95

# Define the number of iterations at each temperature level
iterations_per_temperature = 100

# Define the initial solution randomly
current_solution = [random.randint(1, 32) for _ in range(len(positions))]

# Define the current cost and best cost
current_cost = sum([employee_costs[current_solution[i] - 1] for i in range(len(positions))])
best_solution = current_solution.copy()
best_cost = current_cost

# Perform Simulated Annealing iterations
temperature = initial_temperature
while temperature > 1:
    for _ in range(iterations_per_temperature):
        # Generate a new neighbor solution by randomly changing one position
        neighbor_solution = current_solution.copy()
        position_to_change = random.randint(0, len(positions) - 1)
        neighbor_solution[position_to_change] = random.randint(1, 32)
        
        # Calculate the cost of the neighbor solution
        neighbor_cost = sum([employee_costs[neighbor_solution[i] - 1] for i in range(len(positions))])
        
        # Calculate the cost difference between the neighbor and current solution
        cost_difference = neighbor_cost - current_cost
        
        # Determine whether to accept the neighbor solution as the new current solution
        if cost_difference < 0 or random.random() < math.exp(-cost_difference / temperature):
            current_solution = neighbor_solution
            current_cost = neighbor_cost
        
        # Update the best solution if necessary
        if current_cost < best_cost:
            best_solution = current_solution.copy()
            best_cost = current_cost
    
    # Cool down the temperature
    temperature *= cooling_rate

# Print the minimum total cost found by Simulated Annealing
print("Minimum total cost:", best_cost)
