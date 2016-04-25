from Problems.RF.rf_runner import hpcc_rf
from Algorithms.GridSearch import grid_search
from Algorithms.Random import random_samples
from Algorithms.LHS import lhs


problems = [hpcc_rf]
algorithms = [grid_search]

# RF Parameters
rf_parameters =[[150, 175,  200], [7,8, 9,  10], [0.5,0.75, 1], [50, 100, 150], [True, False]]


for algorithm in algorithms:
    for problem in problems:
        algorithm(rf_parameters, problem)
