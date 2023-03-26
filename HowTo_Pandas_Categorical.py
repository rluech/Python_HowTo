import pandas as pd
import numpy as np

# create by scratch:
d = pd.Series(list('abcd'), dtype='category')
d.dtypes

d = pd.DataFrame({'A': list('abcd'), 'B': list('WXYZ')}, dtype='category')
d
d.dtypes

# from dataframe column:
d = pd.DataFrame({'A': list('abcd')})
d['B'] = d.A.astype('category')
d.dtypes

# from cut(), cut returns dtype category
d = pd.DataFrame({'age': np.random.randint(0, 100, 4000)})
d['ageclass'] = pd.cut(
    d.age, bins=range(0, 101, 10), right=False,
    labels=["{:02d}to{:02d}".format(i, i+9) for i in range(0, 100, 10)]
)
d
d.value_counts().sort_index()  # Ok
d.dtypes

# pandas.Categorical
raw = pd.Categorical(values=list('abcd'),
                   categories=["b", "c", "d"],
                   ordered=False)
d = pd.DataFrame({'A': list('abcd'), 'B': raw})
d
d.dtypes

d = pd.DataFrame({'A': list('abca'), 'B': list('xyzx')})
d = d.astype('category')   # same

# --- ordered category:
tp = pd.CategoricalDtype(categories=list("abcd"), ordered=True)
d['A'] = d['A'].astype(tp)
d['A']

# --- Back to original
d['A'] = d['A'].astype('str')
d['A']

# The accessors .dt and .str will work