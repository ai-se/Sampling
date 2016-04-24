def grid_search(paramters, problem):
    result_filename = "./Result/GridSearch_" + problem.__name__
    fd = open(result_filename, "w")
    import itertools
    parameter_combinations = list(itertools.product(*paramters))
    for parameter_combination in parameter_combinations:
        result = problem(parameter_combination)
        result_line = ",".join(map(str, parameter_combination)) + "|" + str(result)
        fd.write(result_line)
	fd.flush()
    fd.close()

if __name__ == "__main__":
    grid_search([[1,2,3],[4,5,6],[7,8,9,10]])
