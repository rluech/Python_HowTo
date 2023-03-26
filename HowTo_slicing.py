'''
Slicing iterables: lists, dictionary, tuples, sets
Slicing syntax:    iterable[start:stop:step]

'start': inclusive, zero-based starts with 0.
'stop':  exclusive
'step':  if negative changes the logic of start and stop!

- indexing returns a scalar, slicing a lists
- indexing gives Out-of-range Error, slicing returns []
- Python slicing excludes stop, Pandas Dataframe includes start and stop
- Slicing builtin-types returns a copy, NumPy array return a view:
'''

x = [11, 12, 13, 14, 15]

# start
x[0]  # 11, first
x[1]  # 12, second
x[-1]  # 15, last
x[-2]  # 14, second last

# stop
x[3:]  # [14, 15]
x[:-3]  # [11, 12]
x[2:-2]  # [13]
x[2:3]  # the same
x[-2:2]  # [], stop before start returns empty list

# step
x[::2]  # [11, 13, 15], returns every second item

# negative step
x[::-1]  # [15, 14, 13, 12, 11] reverses the sequence
x[1::-1]  # [12, 11] start at 1, all backwards
x[-3::-1]  # [13, 12, 11] start at last 3rd (inclusive) all backwards

# confusing:
x[::-1]  # [15, 14, 13, 12, 11]
x[0:5:-1]  # [] why not the same?
x[5:0:-1]  # [15, 14, 13, 12] cannot stop lower than 0
x[5:-6:-1] # [15, 14, 13, 12, 11] that's it

# Think:
# If step is negative, start has to be after stop in the sequence.
# This is independent of using positive or negative values for start and stop.
# backwards to negative stop in the python zero based fashion len+1 to include the last"

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
#   0   1   2   3   4   5
#  -6  -5  -4  -3  -2  -1

# Slicing builtin-types returns a copy (NumPy array return a view):
a = [1,2,3]
b = a         # no copy
b = a[:]      # slicing: shallow copy (a[] is not allowed, minimum is :)
b = copy(a)   # same
b = a.copy()  # same
