'''
We use tuples to hold together multiple objects.
A tuple is very similar to a list. The 2 main differences are:
- To define a tuple, use parentheses instead of square brackets.
- Once you define a tuple, you cannot change its components.
'''

# --- tuple creation ---

t = tuple()
t = ()
t = (1,)  # comma is needed to create a tuple with only one item.
t = (1, 2)
t = (1, "a")  # different types
t = ((1, 2), (3, 4))  # nested

# --- tuple subsetting ---

t[0]  # indexing
t[0][0]  # nested indexing
t[0:1]  # slicing
# One item: indexing returns a scalar, slicing a tuple

# --- find value in tuple ---
100 in (50, 100)  # True
('A', 'B').index('B')  # 1

# --- change a tuple ---

# t[0] = 100  # TypeError: 'tuple' object does not support item assignment
# t.append(10)  # does not exist
# workaround to update or delete a tuple item is to convert to list and back.

# --- join tuples ---
t + t
t.__add__(t)  # same

# --- tuple comprehension ---

t = 1,2,3
# t / 2  # TypeError: unsupported operand
[x/2 for x in t]  # list comprehension
tuple(x/2 for x in t)  # tuple comprehension, needs tuple()

# --- Tuple packing and unpacking ---
t = 'a', 'b', 'c'  # packing
x, y, z = t  # unpacking
y, x = x, y  # swap two varables

# Often used to return multiple values from a function:
def greet(name):
    hello = "Hello {}".format(name)
    length = len(name)
    return hello, length  # packed into a tuple

message, name_length = greet('Laurent')


