#1. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


tuple1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] #unsorted tuples as input.

sorted_tuple1 = sorted(tuple1, key=lambda x: x[-1]) #key parameter to extract last element of tuple

print("sorted tuple is:",sorted_tuple1)
