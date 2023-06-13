import numpy as np

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

# Define the PSO parameters
num_particles = 50
max_iterations = 100
c1 = 2.0  # cognitive parameter
c2 = 2.0  # social parameter
w = 0.7   # inertia weight

# Define the fitness function to minimize the total cost
def fitness_function(positions, particle):
    total_cost = 0
    for position, employees in positions.items():
        assigned_employees = [employee for idx, employee in enumerate(particle) if idx + 1 in employees]
        if len(assigned_employees) == 0:
            total_cost += min(employee_costs)
        else:
            total_cost += sum([employee_costs[emp - 1] for emp in assigned_employees])
    return total_cost

# Initialize particles randomly
particles = np.random.randint(low=1, high=33, size=(num_particles, len(positions)))

# Initialize velocities as zeros
velocities = np.zeros((num_particles, len(positions)))

# Initialize the best-known positions and the corresponding costs
personal_best_positions = particles.copy()
personal_best_costs = np.array([fitness_function(positions, particle) for particle in particles])

# Initialize the global best position and the corresponding cost
global_best_position = particles[personal_best_costs.argmin()].copy()
global_best_cost = personal_best_costs.min()

# Perform PSO iterations
for _ in range(max_iterations):
    for i in range(num_particles):
        # Update the particle's velocity
        velocities[i] = (w * velocities[i] +
                         c1 * np.random.random() * (personal_best_positions[i] - particles[i]) +
                         c2 * np.random.random() * (global_best_position - particles[i]))
        
        # Update the particle's position
        particles[i] = np.clip(particles[i] + velocities[i], 1, 32)
        
        # Update personal best and global best if necessary
        cost = fitness_function(positions, particles[i])
        if cost < personal_best_costs[i]:
            personal_best_positions[i] = particles[i].copy()
            personal_best_costs[i] = cost
            if cost < global_best_cost:
                global_best_position = particles[i].copy()
                global_best_cost = cost

# Print the minimum total cost found by PSO
print("Minimum total cost:", global_best_cost)
