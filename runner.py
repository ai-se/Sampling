from Problems.RF.rf_runner import hpcc_rf
from Algorithms.GridSearch import grid_search
from Algorithms.Random import random_samples
from Algorithms.LHS import lhs


problems = [hpcc_rf]
algorithms = [grid_search, random_samples, lhs]

# RF Parameters
rf_parameters =[[100], [7], [1], [50], [True, False]]


for algorithm in algorithms:
    for problem in problems:
        algorithm(rf_parameters, problem)