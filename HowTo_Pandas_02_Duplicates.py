import pandas as pd

na = pd.to_numeric(pd.NA)
d = pd.DataFrame({
    "A": ['A', 'A', 'C', 'B', 'B'],
    "B": ['B', 'B', 'C', 'A', 'A'],
    "V1": [12, 12, 17, 33, 32],
})

d
d.duplicated()                              # Returns boolean Series
d.duplicated(subset=['A','B'])              # select columns to consider dups
d.duplicated(subset=['A','B'], keep=False)  # keep: 'first', 'last', False

d.drop_duplicates()
d.drop_duplicates(ignore_index=True)
d.drop_duplicates(ignore_index=True, subset=['A','B'])
d.drop_duplicates(ignore_index=True, subset=['A','B'], keep='last')

# Usecase: print each set of dulicated rows:
dup_ix = [i for i, x in enumerate(d.duplicated(subset=['A','B'])) if x]
for i in dup_ix: 
    print(d.iloc[slice(i-1, i+1)], '\n')

# unique
d.value_counts()
d.V1.value_counts(dropna=False)
d.nunique()                      # on DataFrame count unique
pd.unique(d.V1)                  # on Series return unique values
set([1,2,2,3])                   # Python return unique values
[*dict.fromkeys([1,2,2,3])]      # same, keep order

