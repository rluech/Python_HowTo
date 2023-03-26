# https://numpy.org/devdocs/user/absolute_beginners.html

import numpy as np

# While tuple and lists can contain different data types
# a NumPy array is of one single data type.

(1,2,"a") # tuple
[1,2,"a"] # list

np.array([1,2,"a"]) # error for numpy array
np.array([1,2,3]).dtype # numeric
np.array(["a","b","c"]).dtype # string

# The NumPy ndarray class is used to represent both matrices and vectors
type(np.array([1,2,3])) # <class 'numpy.ndarray'>

np.array([1,2])                          # 1D-array or "vector", single dimension
np.array([[1,2], [4,5], [7,8]])          # 2D-array or "matrix", two dimension
np.array([[[1,2],[3,4]], [[6,7],[8,9]]]) # ndarray  or "tensor", n dimension

x = np.array([[1,2], [4,5], [7,8]])
x.ndim   # 2: number of axis / dimensions
x.shape  # (3,2): tree rows and two columns, two dimensions or "axis"
x.dtype  # dtype('int32')
x.size   # 6
x.T      # Transposed matrix: (2, 3): two rows and three column

x[0,0]       # the element in first row, first column
x[:,1]       # the second column
x[::-1,::-1] # in reverse order

# ! different arrays can share the same data,
# so changes made on one array might be visible in another
y = x[:,1]
y[0] = 9
y
x
np.copy(x)

# Array creation routines: https://numpy.org/devdocs/reference/routines.array-creation.html#routines-array-creation

np.array([1, 2, 3])
np.zeros((2,2))
np.ones((3,3,3), 'int')  # default dtype is float
np.empty((2,2))          # very fast, random number depending on state of the memory
np.arange(4)             # 0,1,2,3
np.arange(2, 9, 2)       # start, stop, step
np.linspace(0, 10, 5)    # 0, 2.5, 5, 7.5, 10
np.full((2,2,2), 'hello')
np.eye(9)

x = np.array([2,1,5,3,7,4,6,8])
np.sort(x)

dtype = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38), ('Galahad', 1.7, 38)]
x = np.array(values, dtype=dtype)  # create a structured array
np.sort(x, order=['age', 'height'])

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a, b))

a = np.array([1, 2], [3, 4])
b = np.array([5, 6])
np.concatenate((a, b), axis=0)

x = np.arange(6)
x.reshape(3, 2)

x = np.arange(6)
np.reshape(x, (3,2), order = 'F') # default is 'C' Row-major, Fortran is column-major