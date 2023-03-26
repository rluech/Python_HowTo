
# A dictionary in Python is made up of key-value pairs (which form items).
# keys must be of type immutable: int, double, str, bool, tuples (no: list, dict, set).
# keys are unique.
# values can be objects of any size, form and type.

# creation
d = {'jack': 4098, 'sjoerd': 4127}
d = {4098: 'jack', 4127: 'sjoerd'}
d = {x: x ** 2 for x in range(10)}
d = dict([('foo', 100), ('bar', 200)])
d = dict(foo=100, bar=200)

a = dict(one=1, two=2)
b = dict({'one': 1, 'two': 2})
c = {'one': 1, 'two': 2}
d = dict({'one': 1}, two=2)
e = dict([('two', 2), ('one', 1)])
f = dict(zip(['one', 'two'], [1, 2]))
a == b == c == d == e == f

k = ('Athens', 'Paris', 'Madrid')
d = dict.fromkeys(k)            # values: 'None'
d = dict.fromkeys(k, 'Europe')  # values: 'Europe'

d = {
    'Brand': ['Ford', 'Audi', 'Honda'],
    'Brand': ['ford', 'audi', 'honda'],  # duplicate key, first will be ignored.
    # ['A']: 'abc',  # mutable key would throw an error
    1:       (6, 8, 4),
    (3,5):   'Car',
    23.7:    [(3,2), None, (5,3)],
    True:    [2.3, 4.3, 1.2]
    }

d.keys()      # class 'dict_keys'
list(d)       # same, as class 'list'
d.values()    # class 'dict_values'
d.items()     # class 'dict_items'
len(d)

# search
'Brand' in d
'Brand' in d.keys()  # same
'Brand' not in d.keys()
'Brand' not in d.values()

# subset
d['Brand']      # error, if 'key' is not found
d.get('Brand')  # safer, if 'key' is not found returns NoneType or a custom value
d[0]            # KeyError: indexing by position not allowed
d[1]            # works if there is a key '1'
[d.get(i) for i in ('Brand', 1, 'NA')]    # subset values by multiple keys
{i: d.get(i) for i in ('Brand',1,'NA')}   # subset items by multiple keys
{key:value for (key,value) in d.items()}  # same, but slow and error if key not found

# add, update
d = {}
d = {'size': 1.83}
if 'size' not in d: d['size'] = 1.54  # prevent from updating an existing key
d.update(weight=83, volume=12)  # add multiple item (or update value if key exists)

b = {'three': 3, 'four': 4}
d.update(b)                  # merge in-place
c = {**d, **b}               # same shallow copy
# d + b                      # TypeError: unsupported

# remove
d = {'A': 1, 'B': 2}
del d['A']
d.clear()  # returns empty dictionary
d.pop('a')  # remove item and return its value, KeyError if not found
d.pop('z', 'Not found')  # catch that error
d.popitem()  # remove and return the last item takes no arguments

# comprehensions

# comprehension with (multiple) if condition and operation on i
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
b = {k:v**2 for (k,v) in d.items() if v>2 if v%2==0}

# if-else example
b = {k:('even' if v%2==0 else 'odd') for (k,v) in d.items()}

# Nested Dictionary comprehension
d = {'first': {'a': 1}, 'second': {'b': 2}}
b = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in d.items()}
