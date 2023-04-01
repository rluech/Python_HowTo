import pandas as pd
import random as rd

# create NA
pd.NA                      # <NA> is 'object', does not coerce to numeric
na = pd.to_numeric(pd.NA)  # returns np.nan ('float', there's no NA-'int' in Pandas)

d = pd.DataFrame({
    "A": ['A', 'A', 'A', 'A'],
    "B": ['B', 'B', na, 'B'],
    "V1": [12, na, na, 32],
    'V2': [1.23, 1.75, 1.54, na],
})

# count NA
d.shape          # count rows and columns
d.info()         # count non-NA elements by column.
d.count()        # same
d.notna().sum()  # same
d.isna().sum()   # inverse
d.isna().agg(['sum','count'])          # same, with counts
d.isna().agg(['sum','count'], axis=1)  # same by rows
d.notna().agg(['sum','count'])         # inverse

# drop NA
d.dropna()                      # drop rows with any NA (default is inplace=False)
d.dropna(how='all')             # drop rows only consisting of NA.
d.dropna(thresh=4)              # keep rows with at least 4 non-NA cells, 'how=' ignored
d.dropna(subset=['B','V1'])     # Columns to look for missing values.
# d = d[d['A'].notna()].copy()  # same
# d = d[~d['A'].na()].copy()    # same

# fill NA
d.fillna(0)                       # replace NA with 0
d.fillna(method="ffill")          # replace NA with last 'ffill' or next 'bfill' valid value.
d.fillna(method="ffill", limit=3) # fill max 3 NA per column or with method= per seq of NA.
d['V1'].fillna(d['V2'])           # fill by another column

d.interpolate()                 # linear interpolation
d.interpolate('spline')         # spline interpolation, see documentation, uses SciPy

# compare NA
d.equals(d)                     # True, equals() treats NaNs as equal
d == d                          # False, NaNs do not compare as equals
d.select_dtypes('number') > 0   # False

# NA in groupby
d.groupby('B').sum()

# NA in count values
d.value_counts(['A','B'], dropna=False)   # d[, .N, k=.(A,B)]

# NA in reduction
d.mean()                    # skipna=True (default)
d.mean(skipna=False)


