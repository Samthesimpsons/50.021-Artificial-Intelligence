''' 1) Implement a CSP that captures the 3 by 3 semi-magic square problem;
Use the file semi-magic.py in the code distribution, which also imports csp.py.  
Variable names: {V1, V2, ... , V9}, indexed row-wise
Domain values: {1, 2, 3}
Constraints:
a) Rowsum, columnsum, and a diagonal sum = 6
b) For each pair of values in the row, column is different (binary constraint)
c) For the diagonal V1, V5, V9 each pair of values is different too (binary constraint) '''

from semimagic import *
import math as m
import pandas as pd

def solve_semi_magic(algorithm=backtracking_search, **args):
    """ From CSP class in csp.py
        vars        A list of variables; each is atomic (e.g. int or string).
        domains     A dict of {var:[possible_value, ...]} entries.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints.
        constraints A function f(A, a, B, b) that returns true if neighbors
                    A, B satisfy the constraint when they have values A=a, B=b
                    """
    # Use the variable names in the figure
    csp_vars = ['V%d' % d for d in range(1, 10)]

    #########################################
    # Fill in these definitions

    csp_neighbors = {'V1': ['V2', 'V3', 'V4', 'V5', 'V7', 'V9'],
                     'V2': ['V1', 'V3', 'V5', 'V8'],
                     'V3': ['V1', 'V2', 'V6', 'V9'],
                     'V4': ['V1', 'V5', 'V6', 'V7'],
                     'V5': ['V1', 'V2', 'V4', 'V6', 'V8', 'V9'],
                     'V6': ['V3', 'V4', 'V5', 'V9'],
                     'V7': ['V1', 'V4', 'V8', 'V9'],
                     'V8': ['V2', 'V5', 'V7', 'V9'],
                     'V9': ['V1', 'V3', 'V5', 'V6', 'V7', 'V8']}

    csp_domains = {}
    for index, var in enumerate(csp_vars):
        csp_domains[var] = [1, 2, 3]

    def csp_constraints(A, a, B, b):
        return a != b

    #########################################

    # define the CSP instance
    csp = CSP(csp_vars, csp_domains, csp_neighbors,
              csp_constraints)

    # run the specified algorithm to get an answer (or None)
    ans = algorithm(csp, **args)

    print('number of assignments', csp.nassigns)
    assign = csp.infer_assignment()
    if assign:
        for x in sorted(assign.items()):
            print(x)
    return csp


if __name__ == '__main__':

    '''2) Attempt to solve with various solution methods'''
    # Options for variable & value ordering, inference
    variable_ordering = [first_unassigned_variable, mrv]
    value_ordering = [unordered_domain_values, lcv]
    inference = [no_inference, forward_checking, mac]

    for i in variable_ordering:
        for j in value_ordering:
            for k in inference:
                print('Variable ordering is {}, value ordering is {} and inference is {}'.format(i.__name__, j.__name__, k.__name__))
                solve_semi_magic(backtracking_search,
                                 select_unassigned_variable=i,
                                 order_domain_values=j,
                                 inference=k)

    '''3) Visualize the number of assignments based on the type of algorithm'''