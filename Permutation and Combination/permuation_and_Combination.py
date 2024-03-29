#import libaries
import itertools

#permutations are the arrangements of objects in a specific order.
#they are concerned with the order in which items are arranged.
#if you have a set of n distinct items and you want to arrange them in a specific order (the order matters), you are dealing with permutations.
#the number of permutations of n distinct items taken r at a time is denoted as P(n, r) or nPr and is calculated as n! / (n - r)!.
#function for permutations
def generate_permutations(elements, r):
    permutations = list(itertools.permutations(elements, r))
    return permutations

#combinations, on the other hand, are concerned with selecting items from a set without considering the order.
#if you have a set of n distinct items and you want to select a specific number of items from this set (e.g., for a group or a team), you are dealing with combinations.
#the number of combinations of n distinct items taken r at a time is denoted as C(n, r) or nCr and is calculated as n! / (r!(n - r)!).
#function for combinations
def generate_combinations(elements, r):
    combinations = list(itertools.combinations(elements, r))
    return combinations

#elements is a list representing the set of elements from which you want to generate permutations and combinations.
#r is the length of the permutations or combinations 
elements = [x for x in range(10, 20)]
r = 2

#calling functions
permutations = generate_permutations(elements, r)
combinations = generate_combinations(elements, r)

print("Permutations:")
for i in permutations:
    print(i)

print("\nCombinations:")
for j in combinations:
    print(j)

# ******************************************************
# Author: Hemant Thapa
# Programming Language: Python
# Date Pushed to GitHub: 01.02.2024
# Email: hemantthapa1998@gmail.com
# ******************************************************
