import pandas as pd
import random as rd

na = pd.to_numeric(pd.NA)
rd.seed(100)

d = pd.DataFrame({
    "A": rd.choices(['blue', 'red'], k=100),
    "B": rd.choices(['frog', 'cat', 'bird'], [1, 2, 3], k=100),
    "V1": rd.choices([*[na] * 10, *range(-45, 45)], k=100),
    "V2": rd.choices([*[na] * 10, *[rd.random() * 100 for x in range(0, 90)]], k=100),
})

d.info()

# count values
d.value_counts(['A', 'B'], dropna=False)  # d[, .N, k=.(A,B)]
d.value_counts(['A', 'B'])  # MultiIndex Series with one level per input column.
d.value_counts(['A', 'B'], normalize=True)  # counts as percentage

pd.cut(d.V1, 4).value_counts()  # 4 equal sized value bins
pd.cut(d.V1, [0, 25, 40, 60, float("inf")]).value_counts()  # cut by value
pd.qcut(d.V1, [0, 0.25, 0.5, 0.75, 1]).value_counts()  # 4 equal sized count bins ('quantiles')

# reduction
d.nunique(dropna=False)
pd.unique(d.V1)
d.min()  # skipna=True (default)
d.max()
d.sum(skipna=False)
d.mean(numeric_only=True)
d.describe()  # numeric columns only
d.describe(include='all')  # all, see d.select_dtypes()

# boolean reduction
(d > 0).all()
(d > 0).any().any()

# which max
d.select_dtypes('number').idxmin(axis=0)  # for each col, return indexname with highest value
d.select_dtypes('number').idxmax(axis=1)  # for each row, return colname with highest value

''' --- Function application ---
Three Functions depending on working on entire DataFrame or Series,
 row- or column-wise, or elementwise:
1. pipe(): Tablewise Function Application, like %>% in R
2. apply(), agg(), transform(): Row or Column - wise Function Application
4. applymap(), map(): Element-wise
'''

d.mean()
d.apply('mean')                                   # same
d.select_dtypes('number').apply('mean')           # same
d.apply(['mean'])                                 # same, reurns dataframe
d.apply('mean', raw=True)                         # Faster, in case indexing is not needed.
d.apply('mean', axis=1, result_type='broadcast')  # choose returned shape, see documentation
d.apply('mean', axis=1)                           # rows
d.apply(['mean', 'sum'])                          # multiple functions
d.apply(pd.Series.interpolate)                    # foreign function
d[['V1', 'V1']].apply(lambda x: x.idxmax())       # own function
def my_fun(x, sub, divide):                       # own function with arguments:
    return (x - sub) / divide
d.apply(my_fun, args=((5,), 3))

d.agg('sum')                                      # same as apply()
d.aggregate('sum')                                # same, agg() is an alias
d.agg(['sum', 'mean'])
d.agg({'V1': ['sum', 'mean'], 'V2': 'var'})       # map to specific columns
d.agg(MyX=('V1', 'mean'), MyY=('V1', 'var'))      # name result

d.transform(['mean'])
d.transform(['abs', lambda x: x + 1])  # duplicate result to return same shape, like data.table
pd.concat([
    d.value_counts(['A', 'B'], dropna=False).to_frame(),
    d.value_counts(['A', 'B'], dropna=False).to_frame().groupby('A').transform(sum)
], axis=1)

'''      Resampler   Rolling    Expanding  ExponentialMovingWindow

'''

'''      
'''


''' applymap():
Note that a vectorized version of func often exists, which will be
much faster, eg.: df ** 2 better than df.applymap(lambda x: x**2)
'''

df = pd.DataFrame([[na, 2.12], [3.356, 4.567]])
def f(x): return len(str(x))

df.applymap(lambda x: len(str(x)), na_action='ignore')
d.applymap(f)
d.V1.map(f)

# --- Sorting ---
# pandas supports three kinds of sorting:
# sorting by index labels: sort_index
# sorting by column values: sort_values()
# and sorting by a combination of both.

import pandas as pd
import numpy as np

d = pd.DataFrame({
    "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
    "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
    "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
})

t = pd.read_csv('data/titanic.csv')

t.sort_values(['Sex', 'Survived'], ascending=[True, False], inplace=True)
t.sort_index(ascending=True)
t.rank(numeric_only=True)
d.sort_values(by='three', na_position='first')
t.nsmallest(3, 'Age').iloc[:, 3:6]
t.nlargest(3, ['Age', 'Fare']).iloc[:, 3:6]

# --- Group By ------------------------------------------------------

t[['Sex', 'Age']].groupby('Sex').mean()
t.groupby('Sex').mean(numeric_only=True)
t.groupby(['Sex', 'Pclass'])['Fare'].mean()

t.groupby('Pclass').size()  # get number of rows within each group
t.Pclass.value_counts(dropna=True)  # same

# nice: return columns instead of Multiindex:
t.groupby(['Sex', 'Pclass'], as_index=False)['Fare'].mean()

# apply on groupby

df = pd.DataFrame({'team': ['A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'points_for': [18, 22, 19, 14, 11, 20, 28],
                   'points_against': [14, 21, 19, 14, 12, 20, 21]})

# find relative frequency of each team name in DataFrame
df.groupby('team').apply(lambda x: x['team'].count() / df.shape[0])

# find max "points_for" values for each team
df.groupby('team').apply(lambda x: x['points_for'].max())

# find max "points_for" values for each team
df.groupby('team').apply(lambda x: (x['points_for'] - x['points_against']).mean())

# --- transform() ---

# Usually groupyby returns a smaller dataframe as the input frame.
# Transform returns like R-data.table the very same shape:

df.groupby('team').mean()  # returns a reduction
df.groupby('team').transform('mean')  # repeated single value
df.groupby('team').transform(lambda x: x - x.mean())  # more useful: normalization within group

df.rename
