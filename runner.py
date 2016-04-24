from Problems.RF.rf_runner import hpcc_rf
from Algorithms.GridSearch import grid_search
from Algorithms.Random import random_samples
from Algorithms.LHS import lhs


problems = [hpcc_rf]
algorithms = [random_samples, lhs]

# RF Parameters
rf_parameters =[[100, 200], [7, 10], [0.5, 1], [50, 150], [True, False]]


for algorithm in algorithms:
    for problem in problems:
        algorithm(rf_parameters, problem)
