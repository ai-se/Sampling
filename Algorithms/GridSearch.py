def grid_search(paramters, problem):
    import itertools
    parameter_combinations = list(itertools.product(*paramters))
    for parameter_combination in parameter_combinations:
        problem(parameter_combination)




if __name__ == "__main__":
    grid_search([[1,2,3],[4,5,6],[7,8,9,10]])