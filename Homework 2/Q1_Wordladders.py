'''Task: Transform the start word into the goal word by 
transforming one letter at a time and all intermediate 
words must be valid as well.

States are strings representing the words'''

import string
from search import *

# List of valid words
WORDS = set(i.lower().strip() for i in open('words2.txt'))

# Helper function to check if the word is valid
def is_valid_word(word):
    return word in WORDS

# Using abstract class for a formal problem from search.py
class Word_Ladders(Problem):

    # list of actions would be the possible words to change from the current state words whereby 
    # it involves changing each letter of the current word and only appending it to the list if it is valid
    def actions(self, state):
        actions = [] #list
        for i,letter_i in enumerate(state):
            for letter_j in string.ascii_lowercase: 
                if letter_i != letter_j:
                    possible_word = state[:i] + letter_j + state[i+1:]
                    if is_valid_word(possible_word):
                        actions.append(possible_word)
        return actions

    def result(self, state, action):
        # return the action (word) itself
        return action

    def value(self, state):
        # not an optimization model, each state has no implicit value
        pass

    # For A* search required to specify the h function in this problem subclass
    def h(self,n):
        # heuristic is how many steps is taken to change to the word
        counter = 0 
        for i in range(len(n.state)):
            # If goal_test fails, aka have not reached goal word, increment counter
            if self.goal_test(n.state) == False:
                counter += 1
        return counter

    def f(self,n):
        # heuristic is how many steps is taken to change to the word
        counter = 0 
        for i in range(len(n.state)):
            # If goal_test fails, aka have not reached goal word, increment counter
            if self.goal_test(n.state) == False:
                counter += 1
        return counter

def get_solution(word_ladder, search_method:str):
    try:        
        if search_method == 'breadth_first_tree_search': #passed
            actions = breadth_first_tree_search(word_ladder).solution() 

        elif search_method == 'depth_first_tree_search': #optimality not reached
            actions = depth_first_tree_search(word_ladder).solution()

        elif search_method == 'depth_first_graph_search': #passed
            actions = depth_first_graph_search(word_ladder).solution()

        elif search_method == 'breadth_first_search': #passed
            actions = breadth_first_search(word_ladder).solution()

        elif search_method == 'best_first_graph_search': #passed
            actions = best_first_graph_search(word_ladder).solution()

        elif search_method == 'uniform_cost_search': #passed
            actions = uniform_cost_search(word_ladder).solution()

        elif search_method == 'depth_limited_search': #passed
            actions = depth_limited_search(word_ladder, limit=50).solution()

        elif search_method == 'iterative_deepening_search': #passed
            actions = iterative_deepening_search(word_ladder).solution()

        elif search_method == 'astar_search': #passed
            actions = astar_search(word_ladder).solution()            

        actions.insert(0,word_ladder.initial)
        print(actions)

    except AttributeError:
        print("Solution not found.")

if __name__ == '__main__':

    ''' Try out all the search methods avaliable
    note the heuristics used for f and h are the same
    and the cutoff for the limited searches are 50'''

    search_methods = [
        'breadth_first_tree_search','depth_first_tree_search',
        'depth_first_graph_search','breadth_first_search','best_first_graph_search',
        'uniform_cost_search','depth_limited_search','iterative_deepening_search','astar_search']
    test_cases = [
        ("cars", "cats"),
        ("cold", "warm"),
        ("best", "math")]

    for search_method in search_methods:
        print(f"Search method: {search_method}")
        for test_case in test_cases:    
            get_solution(Word_Ladders(test_case[0],test_case[1]), search_method)