
# https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping

import pandas as pd

d = pd.read_csv('data/air_quality_long.csv', parse_dates=True)
d.head()

''' --- long to wide ----------------------------------------------------------

melt(frame, id_vars=None, value_vars=None, var_name=None, 
     value_name='value', col_level=None, ignore_index=True)
  Unpivot a DataFrame from wide to long format, optionally leaving 
  identifiers set.

wide_to_long()
  A wrapper to melt(), less flexible.
  
pivot(*, index=None, columns=None, values=None) 
  is simply reshaping, no aggregation.
  Return reshaped DataFrame organized by given index / column values.
  
pivot_table(values=None, index=None, columns=None, aggfunc='mean', ...) 
  Can also aggregate. Is a generalization of pivot(). 
  Can handle Duplicates in index where pivot() cannot.
  Return a spreadsheet-style pivot table as a DataFrame.
  The levels in the pivot table will be stored in MultiIndex objects
  (hierarchical indexes)
  
pd.crosstab(factor, factor, ...)
  Compute a simple cross tabulation of two (or more) factors.
  
stack(level=- 1, dropna=True)
  Return a reshaped DataFrame or Series having a multi-level index.
  
unstack(level=- 1, fill_value=None)
  Pivot a level of the (necessarily hierarchical) index labels.
  Returns a DataFrame having a new level of column labels whose 
  inner-most level consists of the pivoted index labels.
  
'''

# --- melt ------------------------------------------------------------
#
# Melts all columns NOT mentioned in id_vars together
# into two columns: A column with the column header
# names and a column with the values itself.

df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})
df
df.melt(id_vars='A')
df.melt(id_vars='A', value_vars=['B','C'])  # same
df.melt(id_vars='A', value_vars='B')  # ignore column 'C'

df.melt(id_vars='A', value_vars='B',  # give column your names
        var_name='my_Varname', value_name='myValname')

# in case of multi-level columns:
df.columns = [list('ABC'), list('DEF')]
pd.melt(df, col_level=1, id_vars=['D'], value_vars=['F'])
pd.melt(df, col_level=1, id_vars=[], value_vars=['D','F','E'])
df.melt()

# --- pivot -------------------------------------------------------

df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})

df
df.pivot(index='foo', columns='bar', values='baz')
df.pivot(index='foo', columns='bar')['baz']  # same

# A ValueError is raised if there are any duplicates:
df.bar = list('AB')*3
df.pivot(index='foo', columns='bar')
# use pivot_table(), it aggregates duplictes using mean()
df.pivot_table(index='foo', columns='bar')
# It fails equally if aggfunc does not aggregate to one value:
df.pivot_table(index='foo', columns='bar', aggfunc=lambda x: x)
# ValueError: Must produce aggregated value

# --- pivot_table() ------------------------------------------------

df = pd.DataFrame({
    "A": ["foo", "foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar"],
    "B": ["one", "one", "one", "two", "two", "one", "one", "two", "two"],
    "C": ["small", "large", "large", "small", "small", "large", "small", "small", "large"],
    "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
    "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]
})


# pivot_table() average all non-numeric column that are not specified:
df.pivot_table(index=['A','B'])  # mean() over 'C'
df.groupby(["A", "B"]).mean()  # same, pivot_table() is directly linked to groupby():

# column-wise aggfunc, and multiple aggfunc:
df.pivot_table(values=['D','E'], index=['A','C'],
               aggfunc={'D': 'mean',
                        'E': [min, max, 'mean']})

cut()

# --- crosstab -------------------------------------------------------

pd.crosstab(df.A, df.B)  # frequency table
pd.crosstab(df.A, df.B, df.E, aggfunc='mean')  # Requires aggfunc if values is specified

# --- stack and unstack -------------------------------------------------------

# closely related to pivot() and melt()
# Designed to work with MultiIndex objects.

# unstack() # Pivot a level of the (necessarily hierarchical) index labels.

import numpy as np
tuples = list(zip(*[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]))
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df2 = df[:4]
df2
stacked = df2.stack()  # like melt()
stacked
stacked.unstack()
stacked.unstack(1)
stacked.unstack(0)
