
# --- read and write tabular data ---

import pandas as pd

d = pd.read_csv('data/titanic.csv')
print(d)
d.head()
d.head(1)
d.dtypes
d.info()  # technical summary
d.describe()  # stats of numeric columns

d.to_excel('data/titanic.xlsx', index=False)
pd.read_excel('data/titanic.xlsx')