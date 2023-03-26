
# A dictionary in Python is made up of key-value pairs (which form items).
# keys must be of type immutable: int, double, str, bool, tuples (no: list, dict, set).
# keys are unique.
# values can be objects of any size, form and type.

# --- dictionary creation ---

d = dict()
d = dict(key='value')

d = {}
d = {'key': 'value'}

print(d)
type(d)  # class 'dict'

k = ('Athens', 'Paris', 'Madrid')
d = dict.fromkeys(k)           # values: 'None'
d = dict.fromkeys(k, 'Europe') # values: 'Europe'
print(d)

d = {
    'Brand': ['Ford', 'Audi', 'Honda'],
    'Brand': ['ford', 'audi', 'honda'],  # duplicate key, first will be ignored.
    # ['A']: 'abc',  # mutable key would throw an error
    1:       (6, 8, 4),
    (3,5):   'Car',
    23.7:    [(3,2), None, (5,3)],
    True:    [2.3, 4.3, 1.2]
    }

print(d)

d.keys()
d.values()
d.items()
len(d)
'Brand' in d # True
'Brand' in d.keys() # same

# --- subsetting dictionaries ---
# indexing a dictionary works only by calling the keys not by integer index.
# .get() is safer than [key]

d['Brand']
d[1]  # ok if there is a key '1'

d['hello']  # KeyError if a key does not exist
if 'hello' in d: d['hello']  # How to avoid KeyError
print(d.get('hello'))  # better, returns 'None' instead KeyError
print(d.get('hello', 'This value does not exist'))  # customize message

# --- multiple items subsetting and comprehensions ---

b = {i: d.get(i) for i in ('Brand',1,'hello')}  # dictionary comprehension
# b = {i: d[i] for i in ('Brand',1,'hello')}  # same but error for non-existing key
# b = {key:value for (key,value) in d.items()}  # same but slow and error for non-existing key
print(b)

# comprehension with (multiple) if condition and operation on i
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
b = {k:v**2 for (k,v) in d.items() if v>2 if v%2==0}

# if-else example
b = {k:('even' if v%2==0 else 'odd') for (k,v) in d.items()}

# Nested Dictionary comprehension
d = {'first': {'a': 1}, 'second': {'b': 2}}
b = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in d.items()}

# --- assign new item

d = {}
d['name'] = 'Joe'
d['size'] = 1.82
d['size'] = 1.79  # key already exists, this just updates the value
if 'size' not in d: d['size'] = 1.79  # prevent from updating an existing key

d = {}
d.update(name='Joe', size=1.82)
d.update(size=1.79)  # just updates value
d.update(name='Rose', size=1.65, job='actor')  # adds new item

# merge
d = {'one': 1, 'two': 2}
b = {'three': 3, 'four': 4}
d.update(b)  # in-place
c = {**d, **b}  # shallow copy
# d + b  # TypeError: unsupported operand type(s) for +: 'dict'

# --- delete item

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
del d['a']
d.clear() # returns empty dictionary
del d  # delete object

# remove an item and return its value
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
v = d.pop('c')
print(d)
print(v)

d.pop('z')  # KeyError if key does not exist
d.pop('z', 'Not found')  # catch that error

# remove and return the last item
d.popitem()  # takes no arguments