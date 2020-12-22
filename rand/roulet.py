import numpy as np
def rouletteWheelSelection(population):
    total=0
    prob=[]
    for p in population:
        total+=p[0]
        prob.append(p[0])
    prob=np.array(prob)/total
    s=np.random.uniform(0,1,1)
    prob=np.add.accumulate(prob)

    prob=np.where(prob>s)
    newpop=population[prob[0][0]]

    return newpop
print(rouletteWheelSelection(np.array([(30, [1, 1, 1, 1, 0]), (15, [0, 1, 1, 1, 1]), (2, [1, 0]), (2, [1, 0])])))