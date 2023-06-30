import random
import logging
# Configure logging
logging.basicConfig(filename='genetic_algorithm.log', level=logging.INFO)

# Read task times from tasks.txt and store them in a dictionary
task_times = {}
with open('tasks.txt') as f:
    for line in f:
        task, time = line.strip().split(',')
        task_times[int(task)] = int(time)
    print(task_times)

# Read task links from tasks_links.txt and store them in a list
task_links = []
with open('tasks_links.txt') as f:
    for line in f:
        from_task, to_task = line.strip().split(',')
        task_links.append((int(from_task), int(to_task)))
    print(task_links)

# Set the number of generations and the population size
generations = 100
population_size =50


# Set the number of steps
steps = 3

# Define the genome as a list of task numbers
genome_length = len(task_times)
genome = list(range(1, genome_length+1))

# Define the fitness function
def fitness(genome):
    total_time = 0
    diffs = []

    for i in range(steps):
        step_tasks = genome[i*genome_length//steps:(i+1)*genome_length//steps]
        print(step_tasks)
        step_time = sum(task_times[t] for t in step_tasks)
        print(step_time)
        total_time += step_time
        print(total_time)
        diffs.append(abs(step_time - total_time)/(i+1))
        print(diffs[i])
    return total_time, sum(diffs), max(diffs), (step_time)

# Define the genetic operations
def selection(population, fitnesses, num_parents):
    sorted_population = [x for _, x in sorted(zip(fitnesses, population))]
    return sorted_population[:num_parents]

def crossover(parents):
    child = parents[0][:]
    start_index = random.randint(0, len(child)-2)
    end_index = random.randint(start_index+1, len(child)-1)
    for i in range(start_index, end_index+1):
        if child[i] not in parents[1][start_index:end_index+1]:
            j = parents[1].index(child[i])
            child[i], child[j] = child[j], child[i]
    return child

def mutation(individual):
    index1, index2 = random.sample(range(len(individual)), 2)
    individual[index1], individual[index2] = individual[index2], individual[index1]
    return individual

# Initialize the population
population = [random.sample(genome, len(genome)) for _ in range(population_size)]

# Run the genetic algorithm
for generation in range(generations):
    fitnesses = [fitness(individual) for individual in population]
    parents = selection(population, fitnesses, 2)
    offspring = [crossover(parents) for _ in range(population_size-2)]
    offspring = [mutation(individual) for individual in offspring]
    population = parents + offspring

    # Log the best fitness in each generation
    best_fitness = min(fitnesses, key=lambda x: x[1])
    logging.info(f'Generation {generation}: Best fitness = {best_fitness[1]}')

# Extract the results
optimal_results = None
results = [fitness(individual) for individual in population]
print(results)
'''
all_results = [r for r in results if isinstance(r[0],list) and all((t1, t2) in task_links for t1, t2 in zip(r[0], r[0][1:]))]
print(all_results)
if all_results:
    optimal_results = [min(all_results, key=lambda r: r[1])]
    print (optimal_results)
else:
    print("no valid solution s found.'''
# Save the results to files
with open('all_results_steps.txt', 'w') as f:
    for i, result in enumerate(results):
        f.write(f'Solution {i+1}:\n')
        f.write(f'Total Time= {result[0]}\n')
        f.write(f'Total_time/Steps = {result[0]//steps:.2f}\n')
        f.write(f'Total differences = {result[1]:.2f}\n')
        f.write(f'Average differences = {result[1]//steps:.2f}\n')
        f.write(f'Max Time = {max(results[3],default=0)}\n')
        f.write(f'Min Time = {min(results[2],default=0)}\n')
        f.write('----------------------------------------------------------\n')
# Save the optimal results to a file
for i,result in enumerate(results):
    if min(results[2]):
        optimal_results = results[i]
print(optimal_results)
with open('optimal_results_steps.txt', 'w') as f:

            for i, result in enumerate(optimal_results):
                f.write(f'Solution {i + 1}:\n')
                f.write(f'Total Time= {optimal_results[0]}\n')
                f.write(f'Total_time/Steps = {optimal_results[0]//steps :}\n')
                f.write(f'Total differences = {optimal_results[1]:}\n')
                f.write(f'Average differences = {optimal_results[1]//steps :}\n')
                f.write(f'Max Time = {(int(optimal_results[3]))}\n')
                f.write(f'Min Time = {(int(optimal_results[2]))}\n')
                f.write('----------------------------------------------------------\n')
