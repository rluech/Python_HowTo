import pandas as pd
import numpy as np

d = pd.DataFrame({
    "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
    "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
    "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
})

t = pd.read_csv('data/titanic.csv')

# --- descriptive statistics ---

d.describe()
t.describe(include='number')  # numeric columns only: see d.select_dtypes()

d.mean()
d.median()
d.sum()
t.max(numeric_only=True)
d.min()

d.idxmin(axis=0)  # if equals retrurns the first
d.idxmax(axis=1)

# Frequencies
t.Sex.value_counts()  # hist
t[['Sex', 'Survived']].value_counts()  # Crosstab
pd.cut(t.Age, [0, 25, 40, 60, float("inf")]).value_counts()  # cut by value
pd.qcut(t.Age, [0, 0.25, 0.5, 0.75, 1]).value_counts()  # cut by quantile

# boolean reduction
(d > 0).all()
(d > 0).any().any()

# Comparing if objects are equivalent
(d + d == d * 2)  # NaNs do not compare as equals
(d + d).equals(d * 2)  # equals() treats NaNs as equal

''' --- Function application ---
Three Functions depending on working on entire DataFrame or Series,
 row- or column-wise, or elementwise:
1. Tablewise Function Application: pipe()
2. Row or Column - wise Function Application: apply()
3. Aggregation API: agg() and transform()
4. Applying Elementwise Functions: applymap()
'''

# pipe() to chain functions application on dataframe, recommended like %>% in R.

# apply(): Row or column-wise function application:
# apply takes a Series (the row or column), with raw=True an ndarray which may be faster
d.apply(np.mean)
d.apply('mean')  # same
d.apply(np.mean, axis=1)
d.apply(pd.Series.interpolate)
d.apply(lambda x: x.idxmax())
d.apply(lambda x: x.max() - x.min())
d.apply(np.sum, axis=1, result_type='broadcast')  # choose returned shape
def my_fun(x, sub, divide): return (x - sub) / divide  # custom function with arguments:
d.apply(my_fun, args=((5,), 3))
d.apply('mean', raw=True)  # Faster, in case indexing is not needed.

# applymap(): elementwise function application to a Dataframe:
# Note that a vectorized version of func often exists, which will be
# much faster, eg.: df ** 2 better than df.applymap(lambda x: x**2)

df = pd.DataFrame([[np.nan, 2.12], [3.356, 4.567]])
df.applymap(lambda x: len(str(x)))
df.applymap(lambda x: len(str(x)), na_action='ignore')

# --- Aggregation API ---
# A concise way for multiple aggregation operations
# Similar API to groupby API, window API, resample API

d.agg('sum')  # Using single function is equivalent to apply()
d.apply('sum')
d.aggregate('sum')  # same, agg() is an alias
d.agg(['sum'])  # returs one column per function
d.agg(['sum', 'mean'])
d.agg({'one': 'sum', 'two': 'mean'})  # Dict to mapp different functions to specific columns
d.agg({'sum of quantity:': 'sum', 'number of items:': lambda x: len(x)})
d.agg({'one': ['sum', 'mean'], 'two': 'var'})
# With mixed dtypes that cannot aggregate, .agg will only take the valid aggregations.
#   This is similar to how .groupby.agg works.
t.agg('mean', numeric_only=True)

d.transform('abs')  # transform() is very similar to agg()
d.transform([np.abs, lambda x: x + 1])

# --- Applying elementwise functions ---
# Since not all functions can be vectorized (accept NumPy arrays and return
# another array or value), the methods applymap() on DataFrame and
# analogously map() on Series accept any Python function taking a single
# value and returning a single value. For example:

def f(x): return len(str(x))
d['one'].map(f)
d.applymap(f)

# Reindexing and altering labels
# Reindex() is the fundamental data alignment method in pandas.
# Some explicit reindex calls can speed up things.
# https://pandas.pydata.org/docs/user_guide/advanced.html#advanced
d2 = d.reindex(index=['b','c','a'], columns=['three','two','one'])
d3 = d.reindex_like(d2)  # to align two objects
d3.equals(d2)

d.align(d2, join='left', )  # similar to join/merge

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
t.nsmallest(3, 'Age').iloc[:,3:6]
t.nlargest(3, ['Age','Fare']).iloc[:,3:6]

# Multiindex
idx = pd.MultiIndex.from_tuples(
    [("a", 1), ("a", 2), ("a", 2), ("b", 2), ("b", 1), ("b", 1)],
    names=["first", "second"]
)
m = pd.DataFrame({"A": np.arange(6, 0, -1)}, index=idx)
m

m.sort_values(by=['second', 'A'])

# Multiindex Column
d.columns = pd.MultiIndex.from_tuples(
    [("a", "one"), ("a", "two"), ("b", "three")]
)
d.sort_values(by=('a', 'two'))

# --- Group By ------------------------------------------------------

t[['Sex', 'Age']].groupby('Sex').mean()
t.groupby('Sex').mean(numeric_only=True)
t.groupby(['Sex', 'Pclass'])['Fare'].mean()

t.groupby('Pclass').size()  # get number of rows within each group
t.Pclass.value_counts(dropna=True)  # same

# nice: return columns instead of Multiindex:
t.groupby(['Sex', 'Pclass'],as_index=False)['Fare'].mean()

# apply on groupby

df = pd.DataFrame({'team': ['A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'points_for': [18, 22, 19, 14, 11, 20, 28],
                   'points_against': [14, 21, 19, 14, 12, 20, 21]})

#find relative frequency of each team name in DataFrame
df.groupby('team').apply(lambda x: x['team'].count() / df.shape[0])

#find max "points_for" values for each team
df.groupby('team').apply(lambda x: x['points_for'].max())

#find max "points_for" values for each team
df.groupby('team').apply(lambda x: (x['points_for'] - x['points_against']).mean())

# --- transform() ---

# Usually groupyby returns a smaller dataframe as the input frame.
# Transform returns like R-data.table the very same shape:

df.groupby('team').mean()  # returns a reduction
df.groupby('team').transform('mean')  # repeated single value
df.groupby('team').transform(lambda x: x - x.mean())  # more useful: normalization within group

df.rename