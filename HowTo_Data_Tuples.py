'''
Tuple is very similar to a list but not mutable (no update of elements).
'''

# creation
t = tuple()
t = (1,)              # comma is needed
t = 1,                # same
t = (1, "a")          # different types
t = ((1, 2), [3, 4])  # nested
t = 'a', 'b'          # packing
x, y = t              # unpacking
y, x = x, y           # swap two variables
def fun(x): return x, x + 1  # often used in functions (but not from lambda)
x, y = fun(2)

# info
len(t)

# subset
t[0]     # returns a scalar
t[0][0]  # nested tuple indexing
t[0:1]   # slicing, returns a tuple

# update
# t[0] = 100    # TypeError: 'tuple' object does not support item assignment
# t.append(10)  # does not exist
# workaround convert to list and back
t = ([1, 2, 3], [3, 2, 1])
t[0][0] = 77              # a nested tuple cann be updated 

# sort
t = (2, 3, 1, 3)
sorted(t, reverse=True)  # returns a list not a tuple

# search
3 in t
3 not in t
t.count(3)
t.index(3)                                   # index of first occurrence
tuple(i for i, x in enumerate(t) if x == 3)  # all occurrences
                                             # tuple comprehension, needs tuple()
# join tuples
t + t
t.__add__(t)  # same
