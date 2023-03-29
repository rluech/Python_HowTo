
import pandas as pd

d['A'].isna().sum()  # 

d['A'] = d['A'].fillna(1).astype(int)  # fill NA with 1

d['A'] = d['A'].fillna(d["B"]) # Fill the missing with values from another column

d = d[d['A'].notna()].copy()  # continue by dropping all rows in a column
d = d[~d['A'].na()].copy()    # same
