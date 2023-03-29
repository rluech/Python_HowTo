# quick reference:
# rbind: d = pd.concat([d1, d2]).reset_index(0)    # rbindlist()
# cbind: d = pd.merge(d1, d2, on='A', how='left')  # join on columns
#        d = d1.merge(d2, on='A', how='left')      # same, as method
#        d = d1.join(d2)                           # join on indexes, not recommended

""" --- concat() --------------------------------------------------------------
pd.concat(
    objs,                 # [df1, df2] a container of objects: DF, Series, Dict.
    axis=0,               # The axis to concatenate along.
    join="outer",         # The other(!) axis will be joined: 'outer' or 'inner'.
    ignore_index=False,   # Resulting table has index 0,1,2,...n along concat axis,
                            on the other axis index is still respected.
    keys=None,            # Resulting table gets additional index labelling each
                            of the object along concat axis.
    levels=None,          # To construct Multiindex, overrides 'keys'.
    names=None,           # Names for the levels in the resulting Multiindex.
    verify_integrity=False,  # Check for duplicates in the new concatenated axis, expensive. 
    sort=False
    copy=True,
)
"""
import pandas as pd
d1 = pd.DataFrame({
        "A": ["a", "a", "b", "b"],
        "B": ["b", "a", "b", "a"],
        "C": ["c", "c", "c", "c"],
        "V": [12, 45, 94, 27],
    }, index=[0, 1, 2, 3])

d2 = pd.DataFrame({
        "A": ["b", "b", "a", "a"],
        "B": ["a", "b", "a", "b"],
        "V": [88, 64, 32, 57],
    }, index=[0, 1, 373, 374])

''' axis=0 (default): add rows, joins columns, like rbindlist() '''
pd.concat([d1, d2])                      # all rows, all cols
pd.concat([d1, d2], ignore_index=True)   # same, return re-indexed 0,1,2,...,n
pd.concat([d1, d2], join='inner')        # all rows, drop different cols
pd.concat([d1, d2], keys=['one','two'])  # label the datasets in Multiindex
pd.concat({'d1':d1, 'd2':d2})            # same
pd.concat([d1, d2],                      # mimic rbindlist(idcols='frame'):
          keys=['d1','d2'],
          names=['frame',None],
          ).reset_index(0).reset_index(0, drop=True)
# to add a Series to rows, you have to make it a Dataframe: 
pd.concat([d1, d1.iloc[3].to_frame().T], ignore_index=True)

''' axis=1: add columns, joins rows on index, like cbind() but with join on rows '''
pd.concat([d1, d2], axis=1, join='inner')  # to understand
pd.concat([d1, d2], axis=1)                # not cbind(), it always joins on rowindex
pd.concat([d1.reset_index(drop=True),      # mimic cbind():
           d2.reset_index(drop=True)],
          axis=1)
# the same rules apply for assign(), it always joins on index: 
d1.assign(x=d2.A.reset_index(drop=True), y=d2.V.reset_index(drop=True))

''' --- merge()  --------------------------------------------------------------
high performance SQL-style join

  pd.merge(
    left,
    right,
    how="inner",
    on=None,
    left_on=None,
    right_on=None,
    left_index=False,
    right_index=False,
    sort=True,
    suffixes=("_x", "_y"),
    copy=True,
    indicator=False,
    validate=None,
)
'''
import pandas as pd
d1 = pd.DataFrame({
        "A": ["a", "a", "b", "b"],
        "B": ["b", "a", "b", "a"],
        "C": ["c", "c", "c", "c"],
        "V": [12, 45, 94, 27],
    }, index=[0, 1, 2, 3])
d2 = pd.DataFrame({
        "A": ["b", "b", "a", "a"],
        "B": ["a", "b", "a", "b"],
        "V": [88, 64, 32, 57],
    }, index=[0, 1, 373, 374])

pd.merge(d1, d2)  # empty, join on intersecting columns, ('A','B','V') in this case.
pd.merge(d1, d2, on=('A','B','V'))    # same
pd.merge(d1, d2, on='A')              # inner-join (default) 
pd.merge(d1, d2, on='A', how='left')  # left-join
pd.merge(d1, d2, left_on='A', right_on='B', how='outer')
pd.merge(d1, d2, left_index=True, right_index=True, indicator=True)  # join on Indexes
pd.merge(d1, d2, on='A', indicator=True)  # column 'merge': 'both','left/right_only'
pd.merge(d1, d2, on='A', how='left', sort=False, copy=False)  # mimic data.table y[x]
d1.merge(d2, on='A')  # same, also available as method.

''' --- join() ----------------------------------------------------------------
join() is intended for quick left index-joins, like Excel VLOOKUP.
Uses merge() internally. Use merge() for join by column.
Only available as method.
'''
d = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']},
                 index=['K0', 'K1', 'K2', 'K3', 'K4', 'K5'])

lookup = pd.DataFrame({'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])

d.join(lookup)                     # left-join on indexes (default)
d.join(lookup, how='inner')        # inner-join on indexes
d.join(lookup, rsuffix='_lookup')  # 'rsuffix': in case columns with same names.
d.reset_index().join(lookup, on='index')  # 'on': for d, a column can be key, but never in lookup.

# Join multiple DataFrames by index at once by passing a list:
d.join([lookup, lookup.rename(columns={'B':'C'})])  # all colnames must differ.
