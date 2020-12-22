import random
from pyeasyga import pyeasyga
import numpy as np
def gen(data,cross_prob,mut_prob):
    #np.random.seed(100)
    n=100

    # initialise the GA
    ga = pyeasyga.GeneticAlgorithm(data,
                                population_size=50,
                                generations=100,
                                crossover_probability=cross_prob,
                                mutation_probability=mut_prob,
                                maximise_fitness=True)

    # define and set function to create a candidate solution representation
    def create_individual(data):
        individual = data[:]
        random.shuffle(individual)
        return individual

    ga.create_individual = create_individual

    # define and set the GA's crossover operation
    # 1 point crossover
    def crossover(parent_1, parent_2):
        crossover_index = random.randrange(1, len(parent_1))
        ch_1a = parent_1[:crossover_index]
        ch_1b = [i for i in parent_2 if i not in ch_1a]
        child_1 = ch_1a + ch_1b

        ch_2a = parent_2[crossover_index:]
        ch_2b = [i for i in parent_1 if i not in ch_2a]
        child_2 = ch_2a + ch_2b

        return child_1, child_2

    ga.crossover_function = crossover

    # define and set the GA's mutation operation
    def mutate(individual):
        mutate_index1 = random.randrange(len(individual))
        mutate_index2 = random.randrange(len(individual))
        individual[mutate_index1], individual[mutate_index2] = individual[mutate_index2], individual[mutate_index1]

    ga.mutate_function = mutate

    # define and set the GA's selection operatio
    def rouletteWheelSelection(population):
        total=0
        prob=[]
        for p in population:
            total+=p.fitness
            prob.append(p.fitness)
        prob=np.array(prob)/total
        s=np.random.uniform(0,1,1)
        prob=np.add.accumulate(prob)

        prob=np.where(prob>s)
        newpop=population[prob[0][0]]

        return newpop
        
        

    ga.selection_function = rouletteWheelSelection


    # define a fitness function
    def fitness (a, data):
        dec=0
        n=len(a)-1
        for i in a:
            dec+=i*(2**n)
            n-=1
        return dec

    ga.fitness_function = fitness       # set the GA's fitness function
    ga.run()                            # run the GA



    # print the GA's best solution; a solution is valid only if there are no collisions
    return ga.best_individual()
if __name__ == '__main__':
    n=100
    data=[np.random.randint(2) for i in range(n)]

    with open("Akhilesh_Yadav_output.csv","w") as f:
        f.write(f"cross_prob,mut_prob,Output\n")
        cross_prob_prob,mut_prob_prob=np.linspace(0,1,10),np.linspace(0,1,10)
        best=0
        i,j=None,None
        for cross_prob in cross_prob_prob:
            for mut_prob in mut_prob_prob:
                output=gen(data,cross_prob,mut_prob)
                if output[0]>best:
                    best=output[0]
                    i,j=cross_prob,mut_prob
                f.write(f"{cross_prob:0.3f},{mut_prob:0.3f},{output[0]}\n")
        f.write(f"best is \n {i:0.3f},{j:0.3f},{best}")