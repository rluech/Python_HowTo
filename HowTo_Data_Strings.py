
# --- String creation ---
#
# Strings are iterable sliceable, immutable

s = str()
s = ''
s = 'Hello World'

len(s)  # 11
'W' in s  # True

s[0]
s[0:5]
s[::-1]

# s[10]   # IndexError
# s[1] = 'z'  # TypeError: 'str' object does not support item assignment

# --- change Capitalization ---

str('Hello World').upper()  # 'HELLO WORLD'
str('Hello World').lower()  # 'hello world'
str('hello world').capitalize()  # 'Hello world'
str('hEllo World').title()  # 'Hello World'
str('Hello World').swapcase()  # 'hELLO wORLD'

# meta characters
print('Hello\n\tWorld\n')
print('Hello\\n\\tWorld\\n')  # escape
print(r'C:\some\name')  # r'' raw string, otherwise \name makes newline
print("It's signe!")  # " and '
print('He sayd "It\'s ok" to her.')  # ' and " and '

# --- manipulate the string ---

str(' Hello ').strip()
str('_Hello_').strip('_')
str('Hello World').removeprefix('Hello')
str('Hello World').removesuffix('World')
str('Hello World').replace('H', 'Z')

str('Hello World').split()  # ['Hello', 'World']
str('Hello World').split('l')  # ['He', '', 'o Wor', 'd']
str('Hello World').partition('l')  # ('He', 'l', 'lo World')
str('Hello\nWorld').splitlines()
str('+').join('123')  # '1+2+3', see below: concatenate tuple to 'str'

# --- search the string ---

len('Hello World')  # 11
str('Hello World').index('H')  # 0
str('Hello World').count('l')  # 3
str('Hello World').find('l')  # True
str('Hello World').endswith('d')  # True
str('Hello World').startswith('Hel')  # True
str('Hello World').startswith(('H','I','J','K'))  # True
str('Hello World').islower()  # False
str('12A45').isnumeric()  # False

# loop over list of string (vectorize)
a = ['name', 'value']
b = ['A', 'B', 'value', 'C', 'name', 'D', 'E']
ix = [i in a for i in b]
b[ix]  # list cannot be indexed by boolean, numpy arrays would work

''' --- real world problems ----------------------------------------------- '''
import pandas as pd
d = pd.DataFrame({"name": ['Irene', 'Maggie', 'Lisa'],
                 'value': ['CHF657.500.-','CHF2,847.700.-','CHF1,038.000.-'],
                  'area': ['23 m2', '121 m2', '63 m2']
                  })

d.name[1].split('g')   # element-wise, python-built-in
d.name.str.split('g')  # vectorized, df.str from pandas works on columns

d[[x.startswith('M') for x in d.name]]  # select rows matching a string
d[d.name.str.startswith('M')]           # same, vectorized
d.query("name.str.startswith('M')")     # same

d['value_num'] = d['value'].str.replace('[^0-9]', '').astype(int)  # clean 'CHF2,847.700.-'
d['area_num'] = d['area'].str.split(' ').str[0].astype(float)      # clean '23 m2'



# --- combining strings: + or .format() or f"" ---

a = 'Jonny'
b = 'Depp'
c = 67
a + ' ' + b + ' is ' + str(c) + ' years old.'
str("{} {} is {} years old.").format(a, b, c)  # Python version <3.6
f"{a} {b} is {c} years old."  # modern, recommended because other types are ok:
c = (23,['A',276])
f"{a} {b} is {c} years old."

# format String
# https://docs.python.org/3/library/string.html#format-string-syntax
# https://www.w3schools.com/python/ref_string_format.asp
def mynum(): return float(3.182034975662637448)
"{:.2f}".format(mynum())

# --- string to other types ---

tuple('Hello')
list('Hello')
dict.fromkeys('Hello')
set('Hello')

# --- string from other types ---

# concatenate a tuple to a string:
str().join(('A', 'B', 'C'))
str('+').join(('A', 'B', 'C'))

str('+').join(('A', 'B', 23))  # join() TypeError: expected 'str'
values = ('A', 'B', 23.2)
str('+').join([str(value) for value in values])  # all to 'str
str('+').join(tuple(map(str, values)))  # the same

data = [(1.2,2.9,3.5), (4.8,5.5,6.3)]  # same, but now for multiple tuples
[tuple(map(str, item)) for item in data]
[tuple([str(x) for x in item]) for item in data]  # same less readable

# --- encoding ---
# str('hällö Würld').encode('UTF-8') # ?
