'''Our goal in these exercises will be to develop a flight search engine, 
similar to that of SkyScanner, but significantly smaller. A flight is 
specified with a starting city and starting time, and a destination city 
and deadline time. Cities are represented as strings and times as integers.

Task: We want to be able to answer queries that are specified with a starting city,
starting time, final destination city and deadline time. The objective is to 
find a sequence of flights that departs from the starting city at the starting 
time or later, and arrive at the destination city before the deadline time.
We will formulate it as a search problem.
'''

''' Part 1: A good choice of state in this problem would be the
Current city and current time '''

from search import *

# Skeleton of flight class
class Flight:
    def __init__(self, start_city, start_time, end_city, end_time):
        self.start_city = start_city
        self.start_time = start_time
        self.end_city = end_city
        self.end_time = end_time
    
    '''Part 2: matches method to return a boolean based on whether or not
    the city and time matches a valid flight i.e., True if there is a flight
    in flightDB that leaves from the specified city at a time later than 
    the specified time.'''
    def matches(self, city_time):
        return self.start_city == city_time[0] and self.start_time >= city_time[1]
        
    def __str__(self):
        return str((self.start_city, self.start_time)) + '->' + str((self.end_city, self.end_time))
    __repr__ = __str__

flightDB = [
    Flight('Rome', 1, 'Paris', 4),
    Flight('Rome', 3, 'Madrid', 5),
    Flight('Rome', 5, 'Istanbul', 10),
    Flight('Paris', 2, 'London', 4),
    Flight('Paris', 5, 'Oslo', 7),
    Flight('Paris', 5, 'Istanbul', 9),
    Flight('Madrid', 7, 'Rabat', 10),
    Flight('Madrid', 8, 'London', 10),
    Flight('Istanbul', 10, 'Constantinople', 10)]

# Formulate as a search problem
class Flight_Itinerary(Problem):
    
    def actions(self, state):
        actions = []
        for flight in flightDB:
            if flight.matches(state):
                # Actions is a list of states that the current place and fly to                
                actions.append((flight.end_city, flight.end_time))
        return actions

    # Similar to Q1
    def result(self, state, action):
        return action

    def value(self, state):
        pass
    
    # Goal test is if we arrived at the final(goal state) destination city before the deadline time
    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] <= self.goal[1]
    
    # path cost would be then the time taken for each flight path
    def path_cost(self, c, state1, action, state2):
        return state2[1] - state1[1] + c

'''Part 3: Define a procedure that returns a path, in the form of a sequence 
of (city, time) pairs, that represents a legal sequence of flights (found inflightDB) 
from start city to end city before a specified deadline.'''

def find_itinerary(start_city, start_time, end_city, deadline):
    flight_itinerary = Flight_Itinerary((start_city, start_time), (end_city, deadline))
    try:
        # Ending locations and time
        flight_plan_end = iterative_deepening_search(flight_itinerary).solution()

        # Starting locations and time
        flight_plan_start = []
        for end_flights in flight_plan_end:
            print(end_flights)
            # Note the search only returns the end location and time of the flight, we need the starting location and time
            for flight in flightDB:
                # Find the matching ending location and time, end flight location and time tuple are unique
                if flight.end_city == end_flights[0] and flight.end_time == end_flights[1]:
                    flight_plan_start.append((flight.start_city, flight.start_time))

        # with the two list form a zip iterables 
        result = zip(flight_plan_start, flight_plan_end)
        
        # return iterable zip as a set in the form of the flightDB
        return set(result)
    except AttributeError:
        print("No possible flight plan found.")

'''Part 4: Going Further, Yes a brute-force approach by first calling the find_itinerary function
with a deadline of 1, and then incrementing it by 1 till a successful path is found will find the
path that arrives the earliest should the path exist

Write a procedure find shortest itinerary that implements this strategy.
Your procedure should take in two arguments, representing the starting city and
destination city, and should return a list of (city, time) tuples representing the
shortest path between the two cities. You may assume that there is at least one
path connecting the two cities.'''

'''Additional Challenge: Minimize the number of times procedure calls find_itinerary'''

if __name__ == '__main__':
    # Test Cases
    print(find_itinerary('Rome', 2, 'London', 15))