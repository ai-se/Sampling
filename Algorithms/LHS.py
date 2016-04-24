def smaller_lhs(no_of_parameters, divs):
    from random import choice
    sample = []
    nop = [[i for i in xrange(divs)] for _ in xrange(no_of_parameters)]
    for i in xrange(no_of_parameters):
        temp = choice(nop[i])
        for i in xrange(no_of_parameters): nop[i].remove(temp)
        sample.append(temp)

    return sample


def lhs(paramters, problem):
    from random import randint, uniform, choice
    result_filename = "./Result/true_lhs_" + problem.__name__
    fd = open(result_filename, "w")

    number_of_divison = 4
    min_max = [[p[0], p[-1]] for p in paramters]
    t_parameter_combinations = []
    parameter_combinations = []

    new_parameters = []
    for i, mmax in enumerate(min_max[:-1]):
        if i!=2:
            div = int((mmax[1] - mmax[0])/number_of_divison)
            new_parameters.append([mmax[0] + i*div for i in xrange(number_of_divison-1)] + [mmax[-1]])
        else:
            div = ((mmax[1] - mmax[0])/number_of_divison)
            new_parameters.append([mmax[0] + i*div for i in xrange(number_of_divison-1)] + [mmax[-1]])

    import itertools
    number_of_samples = len(list(itertools.product(*paramters)))
    for _ in xrange(int(number_of_samples/2)):
        indexes = smaller_lhs(len(paramters)-1, number_of_divison)
        temp = []
        for new_parameter, index in zip(new_parameters, indexes):
            temp.append(new_parameter[index])
        t_parameter_combinations.append(temp)

    t_parameter_combinations.sort()
    t_parameter_combinations = list(k for k,_ in itertools.groupby(t_parameter_combinations))

    for i in [True]:
        for tp in t_parameter_combinations:
            parameter_combinations.append(tp + [i])
    print "Number of Combinations: ", len(parameter_combinations)
    for parameter_combination in parameter_combinations:
        result = problem(parameter_combination)
        result_line = ",".join(map(str, parameter_combination)) + "|" + str(result) + "\n"
        fd.write(result_line)
	fd.flush()
    fd.close()

if __name__ == "__main__":
    lhs([[100, 125, 150, 175, 200],[4,5,6, 7, 8],[0.5, 0.6, 0.7, 0.8, 0.9, 1.0], [100, 125, 150, 175, 200], [True, False]], None)
