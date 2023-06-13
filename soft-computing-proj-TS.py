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

# Define the Tabu Search parameters
num_iterations = 100
tabu_list_size = 10

# Initialize the current solution randomly
current_solution = [random.randint(1, 32) for _ in range(len(positions))]

# Initialize the tabu list
tabu_list = []

# Define the best solution and best cost
best_solution = current_solution.copy()
best_cost = sum(employee_costs[current_solution[i] - 1] for i in range(len(positions)))

# Perform Tabu Search iterations
for _ in range(num_iterations):
    # Generate candidate solutions by exploring the neighborhood
    candidate_solutions = []
    for i in range(len(positions)):
        for j in range(1, 33):
            if current_solution[i] != j:
                candidate_solution = current_solution.copy()
                candidate_solution[i] = j
                candidate_solutions.append(candidate_solution)
    
    # Evaluate the candidate solutions and select the best non-tabu solution
    best_candidate_solution = None
    best_candidate_cost = float('inf')
    for candidate_solution in candidate_solutions:
        candidate_cost = sum(employee_costs[candidate_solution[i] - 1] for i in range(len(positions)))
        if candidate_cost < best_candidate_cost and candidate_solution not in tabu_list:
            best_candidate_solution = candidate_solution
            best_candidate_cost = candidate_cost
    
    # Update the current solution
    current_solution = best_candidate_solution
    
    # Update the tabu list
    tabu_list.append(current_solution)
    if len(tabu_list) > tabu_list_size:
        tabu_list.pop(0)
    
    # Update the best solution if necessary
    if best_candidate_cost < best_cost:
        best_solution = best_candidate_solution
        best_cost = best_candidate_cost

# Print the minimum total cost found by Tabu Search
print("Minimum total cost:", best_cost)
