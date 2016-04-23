def random_samples(paramters, problem):
    from random import randint, uniform, choice
    result_filename = "./Result/RandomSamples_" + problem.__name__
    fd = open(result_filename, "w")
    import itertools
    number_of_samples = len(list(itertools.product(*paramters)))
    min_max = [[p[0], p[-1]] for p in paramters]
    parameter_combinations = []
    for _ in xrange(number_of_samples):
        parameter_combinations.append([randint(min_max[0][0], min_max[0][-1]), randint(min_max[1][0], min_max[1][-1]),
                                       round(uniform(min_max[2][0], min_max[2][-1]), 3), randint(min_max[3][0], min_max[3][-1]),
                                       choice(paramters[-1])])

    for parameter_combination in parameter_combinations:
        result = problem(parameter_combination)
        result_line = ",".join(map(str, parameter_combination)) + "|" + str(result)
        fd.write(result_line)
    fd.close()

if __name__ == "__main__":
    random_samples([[100, 125, 150, 175, 200],[4,5,6],[0.5, 0.6, 0.7, 0.8, 0.9, 1.0], [100, 125, 150, 175, 200], [True, False]], None)