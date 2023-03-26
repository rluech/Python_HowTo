import pandas as pd

df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
}, index=[0, 1, 2, 3])
df2 = pd.DataFrame({
    "A": ["A4", "A5", "A6", "A7"],
    "B": ["B4", "B5", "B6", "B7"],
    "C": ["C4", "C5", "C6", "C7"],
    "D": ["D4", "D5", "D6", "D7"],
}, index=[4, 5, 6, 7])
df3 = pd.DataFrame({
    "A": ["A8", "A9", "A10", "A11"],
    "B": ["B8", "B9", "B10", "B11"],
    "C": ["C8", "C9", "C10", "C11"],
    "D": ["D8", "D9", "D10", "D11"],
}, index=[8, 9, 10, 11])

d = pd.concat([df1, df2, df3])  # concat makes a full copy
d
d = pd.concat([df1, df2, df3], keys=["x", "y", "z"])
d.loc['y']
d = pd.concat({"x": df1, "y": df2, "z": df3})  # same
d.reset_index(level=0, names='origin')  # index to column

# Appending rows: convert row into a DataFrame and use concat:
s2 = pd.Series(["X0", "X1", "X2", "X3"], index=["A", "B", "C", "D"])
pd.concat([df1, s2.to_frame().T], ignore_index=True)

# --- concat along axis=1 ---

pd.concat([df1, df2, df3], axis=1)  # default: outer join

df4 = pd.DataFrame({
    "B": ["B2", "B3", "B6", "B7"],
    "D": ["D2", "D3", "D6", "D7"],
    "F": ["F2", "F3", "F6", "F7"],
}, index=[2, 3, 6, 7])

pd.concat([df1, df4], axis=1)  # outer join
pd.concat([df1, df4], axis=1, join='inner')  # inner join

df1.index
df4.index
df4.reindex(df1.index)
pd.concat([df1, df4.reindex(df1.index)], axis=1, join='inner')

# Ignoring indexes on the concatenation axis:
pd.concat([df1, df4], ignore_index=True, sort=False)

# concat a Series to a DataFrame
s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")
pd.concat([df1, s1], axis=1)

s1.name = None
pd.concat([df1, s1, s1, s1, s1], axis=1)  # enumerated colnames

pd.concat([s1, s1, s1], axis=1, keys=['red', 'blue', 'green'])  # rename


