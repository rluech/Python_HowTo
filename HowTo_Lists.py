
'''
A list is a collection of items (iterable).
A list is ordered and subset by index.
A list can hold different data types and can be nested.
A list can be changed (mutable), eg. update items
'''

# creation
l = list()
l = ['A']
l = ['A', 0.5]              # any type
l = ['A', ["B", "A"]]       # nested list
list('ABC')                 # from string (iterable)
list(('A','B'))             # from tuple (iterable)
list({'A': 'a', 'B': 'b'})  # from dictionary (iterable)
list({'A','B'})             # from set (iterable)

# subset
l[0]     # returns a scalar
l[1][0]  # nested list index
l[0:1]   # slicing, returns a list

# update
l[1] = 'A'
l[0:2] = ['A','B']

# add
l[len(l):] = ['X','Y']  # append at the end
l.extend(['X','Y'])     # append at the end (in-place)
l.append('X')           # append at the end, only one item (in-place)
l.insert(0, 'X')        # append at specified position, only one item (in-place)
l + l                   # merge two lists
[*l, *l]                # same, unpacking operator *, Python >= 3.5
l += l                  # merge two lists (in-place)

# remove
l.remove('A')           # remove first occurrence, Error if not found
l.pop(1)                # remove and return item at last or specified position
l.clear()               # remove all items from the list
del l[:]                # same

# sort (in-place)
l.sort()
l.sort(reverse=True)
l.reverse()  # same

# search a list
'A' in l      # True, Is any 'A' in the list
l.count('A')  # 2,    How many 'A' are in the list
l.index('A')  # 0,    Return index of first occurence of 'A', Error if not found
[i for i, x in enumerate(l) if x == "A"]  # [0, 3], all occurence

# Using Lists as Stacks
# Last element added is the first element retrieved (“last-in, first-out”)
stack = [3, 4, 5]
x = 6
stack.append(x)
x = stack.pop()

# Using Lists as Queues
# First element added is the first element retrieved (“first-in, first-out”)
# lists are not efficient for this purpose, doing inserts or pops from
# the beginning of a list is slow.
# Use: from collections import deque

# List Comprehensions
# Create new list form applying an operation to each element of an iterable.
# Or, create a subsequence of those elements that satisfy a certain condition.
# Syntax: [expression for ...]

[x**2 for x in range(5)]             # list comprehension

list(map(lambda x: x**2, range(5)))  # same, a funcion mapping

y = []
for x in range(5): y.append(x**2)     # same, a for loop
# the order of for and ifs is the same for comprehension and loop.

[x*2 for x in range(3)]          # apply an operation to each element ("vectorize")
[abs(x) for x in [-4, -2]]       # apply a function
[x.lower() for x in ['A','B']]   # apply a method
[(x, x**2) for x in range(6)]    # create tuples
[str(round(3.14159, i)) for i in range(1, 6)]

# filter
[x for x in [-2,0,2] if x >= 0]

# flatten a list using a listcomp with two 'for':
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

# combine the elements of two lists if they are not equal:
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# The initial expression in a list comprehension can be any arbitrary
# expression, including another list comprehension:
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
[[row[i] for row in matrix] for i in range(4)]  # transpose rows and columns
# But built-in functions are much better than complex flow statements:
list(zip(*matrix))