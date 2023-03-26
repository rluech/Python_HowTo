'''
A set is an unordered collection with no duplicate elements.
Basic uses include membership testing and eliminating duplicate entries.
'''

a = set()
a = {'A','B','C'}
a = set('ABCA')  # duplicates will be ignored

'A' in a
'A' not in a

a = set('ABC')
b = set('BCD')
a | b  # union
a & b  # intersection
a - b  # difference
a ^ b  # symmetric difference

c = set('BEF')
a | b | c
a & b & c
a - b - c
a ^ b ^ c

# multiple sets
sets = [{5, 3, 2, 6, 1}, {7, 5, 3, 8, 2}, {9, 3}, {0, 3, 6, 7}]
set.intersection(*sets)
set.union(*sets)
from functools import reduce
reduce(lambda a, b: a.symmetric_difference(b), sets)
