import numpy

# This project is extended and a library called PyGAD is released to build the genetic algorithm.
# PyGAD documentation: https://pygad.readthedocs.io
# Install PyGAD: pip install pygad
# PyGAD source code at GitHub: https://github.com/ahmedfgad/GeneticAlgorithmPython
class GA():
    def __init__(self,num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes) -> None:
        super().__init__()
        self.num_generations=num_generations,
        self.num_parents_mating=num_parents_mating,
        self.fitness_func=fitness_function,
        self.sol_per_pop=sol_per_pop,
        self.num_genes=num_genes,
        self.init_range_low=init_range_low,
        self.init_range_high=init_range_high,
        self.parent_selection_type=parent_selection_type,
        self.keep_parents=keep_parents,
        self.crossover_type=crossover_type,
        self.mutation_type=mutation_type,
        self.mutation_percent_genes=mutation_percent_genes
    
    def cal_pop_fitness(self,equation_inputs, pop):
        # Calculating the fitness value of each solution in the current population.
        # The fitness function caulcuates the sum of products between each input and its corresponding weight.
        fitness = numpy.sum(pop*equation_inputs, axis=1)
        return fitness

    def select_mating_pool(self,pop, fitness, num_parents):
        # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
        parents = numpy.empty((num_parents, pop.shape[1]))
        for parent_num in range(num_parents):
            max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
            max_fitness_idx = max_fitness_idx[0][0]
            parents[parent_num, :] = pop[max_fitness_idx, :]
            fitness[max_fitness_idx] = -99999999999
        return parents

    def crossover(self,parents, offspring_size):
        offspring = numpy.empty(offspring_size)
        # The point at which crossover takes place between two parents. Usually it is at the center.
        crossover_point = numpy.uint8(offspring_size[1]/2)

        for k in range(offspring_size[0]):
            # Index of the first parent to mate.
            parent1_idx = k%parents.shape[0]
            # Index of the second parent to mate.
            parent2_idx = (k+1)%parents.shape[0]
            # The new offspring will have its first half of its genes taken from the first parent.
            offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
            # The new offspring will have its second half of its genes taken from the second parent.
            offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
        return offspring

    def mutation(self,offspring_crossover):
        # Mutation changes a single gene in each offspring randomly.
        for idx in range(offspring_crossover.shape[0]):
            # The random value to be added to the gene.
            random_value = numpy.random.uniform(-1.0, 1.0, 1)
            offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value
        return offspring_crossover
        