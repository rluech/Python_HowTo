import pandas as pd
d = pd.DataFrame({"A": ["A0","A1","A2","A3"],
                  "B": ["B0","B1","B2","B3"]
                  }, index=['X0','X1','X2','X3'])

d.index                 # Index-Object
d.index.values          # array
d.index.names           # FrozenList

d.columns               # Index-Object
d.columns.values        # array
d.columns.names         # FrozenList

d.index = [0,1,2,3]     # rename the index
d.columns = ['C','D']   # rename the columns
d.columns[0] = ['A']    # rename single  column, must be a list
d.rename_axis(index='rows', columns='cols')  # rename the index header

d.reset_index(inplace=True)         # move index to column, see drop=True
d.set_index('index', inplace=True)  # move column to index

d.reindex(index=['X3','X4'])    # basically a right join on new indexes, see examples
d.reindex(columns=['B','C'])    # same, on columns
d.reindex_like(d)               # indexed from an other DataFrame

d.sort_index()                  # sort the whole dataframe, lowest on top
d.sort_index(ascending=False)   # highest on top
