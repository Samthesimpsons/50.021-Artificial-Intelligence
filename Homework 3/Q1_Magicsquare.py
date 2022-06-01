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
import random

random.seed(2022) # for reproducibility of results when grading

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
    '''
    1 2 3
    4 5 6
    7 8 9
    '''
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
        # note this will already cover the sum to 6 constraint given the neighbors
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

    df = pd.DataFrame(columns=["Variable_Ordering","Value_Ordering", "Inference", "Number_Assignment"])

    for i in variable_ordering:
        for j in value_ordering:
            for k in inference:
                print('Variable ordering is {}, value ordering is {} and inference is {}'.format(i.__name__, j.__name__, k.__name__))
                result = solve_semi_magic(backtracking_search,
                                          select_unassigned_variable=i,
                                          order_domain_values=j,
                                          inference=k)
                df.loc[len(df)] = [i.__name__, j.__name__,k.__name__, result.nassigns]
                result

    '''3) Visualize the number of assignments based on the type of algorithm'''
    print(df)

'''As we can see from the dataframe results:

mrv                      lcv      no_inference                 24
mrv                      lcv  forward_checking                  9
mrv                      lcv               mac                  9

Firstly if there is both variable and value ordering (mrv and lcv), we note that the case of no inference performed worse than the cases of foward checking or arc consistency checks,
24>9. This is expected as forward checking helps reduce the number of searches, hence assignment since it terminates the search when any variable has no more legal values.
Arc consistency repeatedly enforces constraints locally via propagation and detects failure earlier than forward checking. Nevertheless, no inference is expected to perform worse than
cases of inferences being applied.

mrv  unordered_domain_values      no_inference                 11
mrv  unordered_domain_values  forward_checking                  9
mrv  unordered_domain_values               mac                  9
A similar pattern is once again observed.

For all the remaining cases, we note that the number of assignments is similar, this might be due to the fact that the 
CSP problem is not very complex in the first place. However, from our run we got to see the effectives of using inferencing.'''