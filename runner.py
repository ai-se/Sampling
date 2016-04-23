from Problems.RF.rf_runner import hpcc_rf
from Algorithms.GridSearch import grid_search


problems = [hpcc_rf]
algorithms = [grid_search]

# RF Parameters
rf_parameters =[[100], [7], [1], [50], "True"]


for algorithm in algorithms:
    for problem in problems:
        algorithm(rf_parameters, problem)