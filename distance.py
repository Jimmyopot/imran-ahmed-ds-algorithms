'''
          Ottawa  Montreal  Kingston  Toronto  Sudbury
Ottawa       -      199       196       450      484
Montreal    199      -        287       542      680
Kingston    196     287        -        263      634
Toronto     450     542       263        -       400
Sudbury     484     680       634       400       -
'''

'''
- Can we generate the travel plan for the salesman? 
- What will be the optimal solution that can minimize the total distance traveled by the traveling salesman?
- Note that the objective is to get a tour that starts and ends in the initial city. 
- For example, a typical tour can be Ottawa–Sudbury–Montreal–Kingston–Toronto–Ottawa with a cost of
484 + 680 + 287 + 263 + 450 = 2,164.
'''
# solution 1 (GREEDY ALGORITHM)

def greedy_algorithm(cities, start=None):
    C = start or first(cities)
    tour = [C]
    unvisited = set(cities - {C})
    
    while unvisited:
        C = nearest_neighbor(C, unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour

def first(collection):
    return next(iter(collection))

def nearest_neighbor(A, cities):
    return min(cities, key=lambda C: distance_points(C, A))

l = greedy_algorithm(3)
print(l)





# solution 2 (BRUTE FORCE)

'''
- There are n number of cities., hence (n-1)! possible tours.
- This means 5 cities will produce 4!=24 tours.
- Evaluate all possible tours.
- Choose the shortest distance.
'''

import random
from itertools import permutations
alltours = permutations

def distance_tour(aTour):
    
    for i in range(len(aTour)):
        return sum(distance_points(aTour[i-1], aTour[i]))

def distance_points(first, second): 
    return abs(first - second)

def generate_cities(number_of_cities):
    seed = 111
    width = 500
    height = 300 
    
    for c in range(number_of_cities):
        aCity = complex
        random.seed((number_of_cities, seed))
        return frozenset(aCity(random.randint(1, width), random.randint(1, height)))