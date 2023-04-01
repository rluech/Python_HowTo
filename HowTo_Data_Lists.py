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
list(('A', 'B'))            # from tuple (iterable)
list({'A': 'a', 'B': 'b'})  # from dictionary (iterable)
list({'A', 'B'})            # from set (iterable)

# pd.Series().tolist()      # to list work for some iterable

# info
len(l)

# subset
l[0]     # returns a scalar
l[1][0]  # nested list index
l[0:1]   # slicing, returns a list

# update
l[1] = 'A'
l[0:2] = ['A', 'B']

# add
l.append('X')            # append one item at the end (in-place)
l.insert(0, 'X')         # same, but at specified position
l.extend(['X', 'Y'])     # append multiple item at the end (in-place)
l[len(l):] = ['X', 'Y']  # same
l += ['X', 'Y']          # same
l + ['X', 'Y']           # same, not in-place
[*l, *['X', 'Y']]        # same, unpacking operator *, Python >= 3.5
l *= 2                   # l repeated n times (in-place)

# remove
l.remove('A')  # remove first occurrence, Error if not found
l[0:2] = []    # remove items at specified position
l.pop(1)       # remove and return item at last or specified position
l.clear()      # remove all items from the list
l[:] = []      # same
del l[:]       # same

# sort (in-place)
l.sort()
l.sort(reverse=True)
l.reverse()  # same

# search a list
'A' in l        # Is any 'A' in the list
'A' not in l
l.count('A')    # How many 'A' are in the list
l.index('A')    # Return index of first occurence of 'A', Error if not found
[i for i, x in enumerate(l) if x == "A"]  # all occurence
l.count(l[0]) == len(l)  # all equal, faster than len(set(l))<=1

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

[x ** 2 for x in range(5)]             # list comprehension
list(map(lambda x: x ** 2, range(5)))  # same, a funcion mapping
y = []
for x in range(5): y.append(x ** 2)    # same, a for loop
# the order of for and ifs is the same for comprehension and loop.

[x * 2 for x in range(3)]        # apply an operation to each element ("vectorize")
[abs(x) for x in [-4, -2]]       # apply a function
[x.lower() for x in ['A', 'B']]  # apply a method
[(x, x ** 2) for x in range(6)]  # create tuples
[str(round(3.14159, i)) for i in range(1, 6)]

# filter
[x for x in [-2, 0, 2] if x >= 0]
['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l]

# flatten a list using a listcomp with two 'for':
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]

# combine the elements of two lists if they are not equal:
[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# The initial expression in a list comprehension can be any arbitrary
# expression, including another list comprehension:
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
[[row[i] for row in matrix] for i in range(4)]  # transpose rows and columns
# But built-in functions are much better than complex flow statements:
list(zip(*matrix))

# zip
# zip() returns an iterator of tuples, where the i-th tuple contains the i-th
# element from each of the argument iterables.
list(zip(range(3), ['A', 'B']))
list(zip(range(2), ['A', 'B'], strict=True))
for x in zip([1, 2, 3], ['A', 'B', 'C']): print(x)
for x in zip([1, 2], ['A', 'B'], (9, 8, 7)): print(x)

# unzip: * and **-operator
list(range(3, 6))   # range() needs separate arguments
args = [3, 6]       # If they are not available separately
list(range(*args))  # unpack the arguments out of a list or tuple

f = lambda x, y='Y', z='Z': print("1:", x, '2:', y, '3:', z)
d = {'x': 'one', 'y': 'two', 'z': "three"}
f(**d)
