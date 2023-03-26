# --- The print Function --- #
print('Hello World')

# --- 4 space Indention instead of curly braces for code block --- #
x = 1
if x == 1:
    print('x is 1')

# --- Numbers --- #
myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# --- Strings --- #

print('Hello')
print("Hello")
print("Don't worry about apostropes")
print('Don\'t worry about apostropes')  # Escape character with "\"

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# one + hello # Mixing types is not supported

# --- Assignment --- #

a, b = 2, 3
print(a, b)

# --- test for data type
mystring = "hello"
myfloat = float(10)
myint = int(20)

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# --- Lists

mylist = []
mylist = [1,2,3]
mylist.append(4)
for x in mylist:  # iterate over lists is very easy
    print(x)
mylist[10] # IndexError: list index out of range
strings = ["Hello"]
strings.append("World")
strings

# --- Arithmetic Operators

number = 1 + 2 * 3 / 4
number
(1 + 2 * 3) / 4

reminder = 11 % 3  # Modulo: %
reminder
11/3

squared = 3 ** 2  # Power: **
cubed = 3 ** 3
squared
cubed

text = "Hello" + " " + "World"  # concatenate Strings
print(text)
lotsofhellos = "Hello" * 10  # multiplying String
print(lotsofhellos)

evennumbers = [2,4,6,8]
oddnumbers = [1,3,5,7]
allnumbers = evennumbers + oddnumbers  # join lists
print(allnumbers)

print([1,2,3] * 3)  # as with Strings, Lists can be multiplied

x = object()
list = [x] * 10
len(list)
list.count(x)

# --- String formatting

name = "John"
print("Hello %s!" % name)
age = 24
print("%s is %d years old." % (name, age))  # use a tuple for multiple variables

print("String: %s oder %s" % ("Eins", 1))  # %s: Strings und Objekte mit string-representation
print("Integer: %d" % 2020)
print("Float: %f" % 3.14)
print("Float: %.2f" % 3.14)
print("Hex: %x" % 15)

# --- Basic String Operations

astring = "Hello world!"
print(len(astring))
print(astring.index("o"))
print(astring.count("l"))
print(astring[3:7])
print(astring[:7])
print(astring[3:])   # head
print(astring[-3:])  # tail
print(astring[:-3])
print(astring[3:7:2])  # [start:stop:step]
print(astring[::-1])  # no rev() in Python, use negative steps instead
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
astring.split(" ")
astring.split("l")

s = "Hey thera! what shou"
# Length should be 20
print("Length of s = %d" % len(s))
# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))
# Number of a's should be 2
print("a occurs %d times" % s.count("a"))
# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s [1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# --- Conditions

x = 2
x == 2
x == 3
x != 3
x < 3
x <= 2
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John and you are 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
if name in ["John", "Rick"]:
    print("Your name is either John or Rick")

# --- code blocks

x = 2
if x == 2:
    print("x is 2.")
elif x > 2:
    print("x is bigger than 2")
else:
    print("x is smaller than 2")

# a statement is evaluated as TRUE if
# 1. the boolean variable TRUE is given or returned from an expression.
# 2. An object which is not considered "empty" is passed.
# Empty objects: empty string "", empty list [], number Zero 0, boolean FALSE.

if x:
    print("x is not empty")

# --- The 'is' operator

# '==' matches the values of the variables
# 'is' matches the instances themselves

x = [1,2,3]
y = [1,2,3]
x == y  # TRUE
x is y  # FALSE

print(not False) # not before a boolean expression inverts it.
(not False) == False

# --- Loops

primes = [1,2,3]
for prime in primes:
    print(prime)

for prime in [1,2,3]:
    print(prime)

for x in range(5):
    print(x)

for x in range(3,5):
    print(x)

for x in range(1,9,3):
    print(x)

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# break is used to exit a for loop or a while loop,
# whereas continue is used to skip the current block,
# and return to the "for" or "while" statement.

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

# We can use "else" for loops, unlike other programming languages

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % count)

# "Else" is skipped if the for loop has a "break" inside

for i in range(10):
    if i % 5 == 0:
        break
    print(i)
else:
    print("this is not printed because for loop is terminated"
          " because of break but not due to fail in condition")

# --- functions

# block_head:
#    1st block line
#    2nd block line
#    ...

# block_keyword block_name(argument1, argument2, ...)
#   Block keywords you already know are "if", "for", and "while".

# Functions in python are defined using the block keyword "def",
#   followed with the function's name as the block's name.

def my_function():
    print("Hello from my function!")

my_function()

# Functions may also receive arguments

def my_function_with_arguments(username, greeting):
    print("Hello, %s, From my function!\n\tI wish you %s" % (username, greeting))

my_function_with_arguments("Rafael", "Happy Birthday")

# Functions may return a value to the caller, using the keyword- 'return'

def sum_two_numbers(a, b):
    return a + b

sum_two_numbers(32, 84)

# --- Classes and Objects

# Objects are an encapsulation of variables and functions
# into a single entity. Objects get their variables and
# functions from classes. Classes are essentially a template
# to create your objects.

class MyClass:  # define a class
    variable = "blah"

    def function(self):
        print("This is a message insde the class.")

myobjectx = MyClass()  # assigne the class to an object
myobjectx.variable
myobjectx.function()

myobjecty = MyClass()  # each object will be an independent copy of the class
myobjecty.variable = "y blah bli blabla"

print(myobjectx.variable)
print(myobjecty.variable)

# The __init__() function, is a special function that is called
# when the class is being initiated. It's used for assigning
# values in a class.

class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'

# --- Dictionaries

# A dictionary is a data type similar to arrays,
# but works with keys and values instead of indexes.
# Each value stored in a dictionary can be accessed using a key,
# which is any type of object (a string, a number, a list, etc.)
# instead of using its index to address it.

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# iterate over a dictionary

for name, number in phonebook.items():
    print("The phone number of %s is %d" % (name, number))

# remove an item

phonebook.pop("Jill")
# or
del phonebook["Jack"]

phonebook.pop(["Jill","Jack"])

print(phonebook)

# --- Modules

# Modules in Python are just Python files with a .py extension.
# A Python module can have functions, classes, variables.
# Modules are imported from other modules using the import command.
# Example:
#
# game.py
# import the draw module
# import draw
#
# def play_game():
#     ...
#
# def main():
#     result = play_game()
#     draw.draw_game(result)
#
# # this means that if this script is executed, then
# # main() will be executed
# if __name__ == '__main__':
#     main()

# When the import draw directive runs, the Python interpreter
# looks for a file in the directory in which the script was
# executed with the module name and a .py suffix

# You may have noticed that when importing a module,
# a .pyc file is created. This is a compiled Python file.
# Python compiles files into Python bytecode so that it
# won't have to parse the files each time modules are loaded.
# If a .pyc file exists, it gets loaded instead of the .py file.
# This process is transparent to the user.

# A namespace is a system where every object is named and can
# be accessed in Python. We import the function draw_game into
# the main script's namespace by using the from command.

# Example:
# from draw import draw_game
#
# def main():
#     result = play_game()
#     draw_game(result)

# The advantages of this notation is that you don't have to reference
# the module over and over. However, a namespace cannot have two objects
# with the same name, so the import command may replace an existing
# object in the namespace.

from draw import * # import all objects from a module

# Modules may be loaded under any name you want.
# This is useful when importing a module conditionally
# to use the same name in the rest of the code:
if visual_mode:
    import draw_visual as draw
else:
    import draw_textual as draw

def main():
    result = play_game()
    draw.draw_game(result)

# The first time a module is loaded into a running Python script,
# it is initialized by executing the code in the module once.
# If another module in your code imports the same module again,
# it will not be loaded again.

# Extending module load path (add paths besides default local
# directory and built-in modules):
PYTHONPATH=/foo python game.py
# or
sys.path.append("/foo") # Execute it before running the import command

# We can look for which functions are implemented in each module
# by using the dir function:
import urllib
dir(urllib)

# When we find the function in the module we want to use, we can read
# more about it with the help function:
help(urllib.urlopen)

# Writing packages
# Packages are namespaces containing multiple packages and modules.
# They're just directories, but with certain requirements.

# Each package in Python is a directory which MUST contain a special
# file called __init__.py. This file, which can be empty, indicates
# that the directory it's in is a Python package. That way it can be
# imported the same way as a module:
# If we create a directory called foo, which marks the package name,
# we can then create a module inside that package called bar.
# Then we add the __init__.py file inside the foo directory.

# The __init__.py file can also decide which modules the package exports
# as the API, while keeping other modules internal, by overriding the
# __all__ variable like so:
__init__.py:
__all__ = ["bar"]

# install packages

# PyCharm: open Python packages Window from bottom meue list.
# enter package name in search field.
# if found, press install button right upper corner.

# install to local python version via shell command using pip installer:
# https://packaging.python.org/en/latest/tutorials/installing-packages/#requirements-for-installing-packages

# --- NumPy

# Numpy arrays are great alternatives to Python Lists. Some of the key
# advantages of Numpy arrays are that they are fast, easy to work with,
# and give users the opportunity to perform calculations across entire arrays.

height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)
print(type(np_height))

np_weight / 3

bmi = np_weight / np_height ** 2
print(bmi)

bmi[bmi > 24]

# --- Pandas

#  It is built on the Numpy package and its key data structure is called
#  the DataFrame. DataFrames allow you to store and manipulate tabular data
#  in rows of observations and columns of variables.

# There are several ways to create a DataFrame.
# One way way is to use a dictionary

dict = {
    "country":    ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital":    ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
    "area":       [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
        }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
brics[['country']]

# Column-names in dataframes are called "index" and by default numeric:

brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# Another way to create a DataFrame is by importing a csv file using Pandas

cars = pd.read_csv("C:/Users/rluec/PycharmProjects/pythonProject/cars.csv")
cars

# Indexing Dataframes
# There are several ways to index a Pandas DataFrame.
# One of the easiest ways is square bracket notation.
# The single bracket returns a Pandas Series, double bracket a Pandas DataFrame.
cars = pd.read_csv("C:/Users/rluec/PycharmProjects/pythonProject/cars.csv", index_col = 0)

print(cars['cars_per_cap'])

# column index
brics['country']             # returns a Series
brics[['country']]           # returns a DataFrame
brics[['country','capital']]

# row index
brics[0:4]
brics[1::2]

# You can also use loc (label index) and iloc (integer index)

brics.iloc[2]     # third row
brics.iloc[2, 3]  # Cell in third row, fourtht column
brics.loc[['BR','RU']]  # Rows by rowname

brics['BR','country']

brics.loc['BR']
brics.loc['BR',:]
brics['BR']
brics.loc['BR',:]

# --- Generators ---

# In Python, similar to defining a normal function, we can define
# a generator function using the def keyword, but instead of the
# return statement we use the yield statement.

def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

type(fib())  # <class 'generator'>

counter = 0
for n in fib():
    print(n)
    counter += 1
    if counter == 10:
        break


def my_generator(n):
    counter = 0
    while counter < n:
        yield counter
        counter += 1

for counter in my_generator(3):
    print(counter)

generator = my_generator(3)
print(next(generator))
print(next(generator))
print(next(generator))

# Python generator expression
# Syntax: (expression for item in iterable)

squares_generator = (i * i for i in range(5))
for i in squares_generator:
    print(i)

# --- List Comprehensions ---

# List Comprehensions is a very powerful tool, which creates
# a new list based on another list, in a single, readable line.

# For example, let's say we need to create a list of integers which
# specify the length of each word in a certain sentence, but only if
# the word is not the word "the".

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))

print(words)
print(word_lengths)

# Using a list comprehension, we could simplify this:
word_lengths = [len(word) for word in words if word != "the"]

# Example 2: create a new list called "newlist" out of the list "numbers",
# which contains only the positive numbers from the list, as integers

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)

# --- lambda functions ---

# An anonymus function to be run at the place of creation.
# Use the key word lambda for creation.
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments,
# but can only have one expression.
# The expression is executed and the result is returned:
# general syntax: my_lambda = lambda inputs : output

def sum_fun(a,b):  # a normal function
    return a + b

sum_lambda = lambda x,y : x + y  # the same, as lambda function

print(sum_fun(1,2))
print(sum_lambda(1,2))

# Example. The power of lambda is better shown when you use them
# as an anonymous function inside another function.

def myfunc(n):
    return lambda a : a * n  # we return a function object

my_doubler_fun = myfunc(n=2)
print(my_doubler_fun(11))

my_trippler_fun = myfunc(n=3)
print(my_trippler_fun(11))

# --- Multiple Function Arguments ---

# Every function in Python receives a predefined number of arguments,
# normally like this:

def myfunction(first, second, third):
    # do something with the 3 variables

# *therest allows to capture all inputs after the first 3 arguments
# *therest is a list of variables:
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))

foo(1, 2, 3, 4, 5, 6)

# It is also possible to send functions arguments by keyword,
# so that the order of the argument does not matter:

def bar(x, y, z, **options):

    if options.get("normalize") == True:
        x, y, z = [i - (x + y + z)/2 for i in [x, y, z]]

    if options.get("action") == "mult":
        print("The multiplication is: %d" % (x*y*z))
    else:
        print("The sum is: %d" % (x+y+z))

bar(1,2,3, action = "sum", normalize = True)
bar(1,2,3)

# Two more Examples:
# The foo function must return the amount of extra arguments received.
# The bar must return True if the argument with the keyword magicnumber
# is worth 7, and False otherwise.

def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7

""" --- Regular Expressions ---
Regular Expressions (sometimes shortened to regexp, regex, or re)
are a tool for matching patterns in text. In Python, we have the re module.
The applications for regular expressions are wide-spread, but they are
fairly complex, so when contemplating using a regex for a certain task,
think about alternatives, and come to regexes as a last resort.
"""

import re

pattern = re.compile(r"\[(on|off)\]") # slight optimization
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]")) # returns a match object
type(pattern)
print(re.search(pattern, "Nada...:-(")) # # returns None
