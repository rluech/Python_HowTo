'''
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html

A DataFrame is a 2-dimensional data structure that can store data of 
different types (including characters, integers, floating point values, 
categorical data and more) in columns. It is similar to a spreadsheet, 
a SQL table or the data.frame in R.
When using a Python dictionary of lists, the dictionary keys will be used 
as column headers and the values in each list as columns of the DataFrame.
Each column in a DataFrame is a Series.
'''

import pandas as pd

d = pd.DataFrame({
  "Name": ["Owen", "William", "Elizabeth"],
  "Age": [22, 35, 58],
  "Sex": ["male", "male", "female"]
})

d.info
d.dtypes

d.shape  # (3, 3)
d.ndim   # 2
len(d)   # 3, the number of rows
d.size   # 12

d.head()
d.tail()

d.describe()               # statistics for numerical columns
d.describe(include='all')
d.Sex.describe()           # statistics for string column

d.columns         # type index , make list: list(d.columns)
d.columns.values  # type array
d.index           # row names

# --- work on Columns ---------------------------------------------------------

# rename column
nm = d.columns
d.columns = nm[::-1]                             # rename all columns
d.set_axis(nm, axis=1, inplace=True)             # rename all columns
d.rename(columns=str.lower, inplace=True)        # rename all columns mapping a function
d.columns = [x.title() for x in d.columns]       # rename all columns mapping a function
d.columns = [x.title() for x in d.columns if x not in ['Sex']]  # rename specific columns
d.columns.values[0] = 'X'                        # rename specific columns, not recommended
d.rename({'Age': 'year'}, axis=1, inplace=True)  # rename specific columns
d.columns = nm

# Selecting a column
d['Age']              # returns a Series
d[['Age']]            # returns a DataFrame
d.Age                 # returns a Series, using the dot operator
d[['Age','Sex']]      # select multiple columns
d.get(['Age','Sex'])  # same as d[['Age','Sex']], catch if 'col' is not found

d.loc[:, 'Name':'Sex']           # label indexing
d.iloc[:, 0:2]                   # integer indexing
d.iloc[:, [False, True, False]]  # boolean indexing
d.iat[0, 1]                      # get single element, # integer indexing
d.at[0, 'Name']                  # get single element, # label indexing
d.xs('Name', axis=1)             # indexing Multiindex DataFrame

d.filter(items=['Age','Sex'])  # same as d[['Age','Sex']]
d.filter(like='a')             # column names with an 'a'
d.filter(regex='\d')           # number in column name

d.select_dtypes('number')                 # select dataframe by columns dtype (copy)
d.select_dtypes('number').columns.values  # select column names only

# Add a column
d['Weight'] = [80, 63, 78]                           # append at the end, don't try: d.Weight =
# d.Weight = [80, 63, 78]                             # no assignment with dot operator
d.insert(1, 'BMI', d['Weight'] / d['Age'] ** 2)  # insert column at specific location
d = d.assign(BMI2=lambda x: x.Weight / x.Age ** 2)   # copy of df with new col, no inplace

# add multiple columns -> join two dataframes
d[['D', 'E']] = pd.DataFrame.from_dict(zip(pd.Series([1,2,3]), pd.Series(['a','b','c'])))  # recommended
d[['D', 'E']] = pd.DataFrame([[1,2,3], ['a','b','c']]).T  # hack
d[['D', 'E']] = [3, 'dogs']  # works
d['X'], d['Y'] = [6, 'birds']
d.assign(F=4, G='cats')
d.join(pd.DataFrame({'F': 4, 'G': 'cats'}, index=d.index))  # join
d.join(pd.DataFrame([[4,'cats']], columns=['F','G'], index=d.index))  # same
pd.concat([d, pd.DataFrame({'F': 4, 'G': 'cats'}, index=d.index)], axis=1)  # concat

# delete column
d.drop(['Weight','BMI2'], axis=1, inplace=True)  # recommended
d.pop('BMI')
del d['Sex']

# reorder columns (copying all data)
d.reindex(columns=['Sex', 'Age', 'Name'])
d = df[df.columns[::-1]]

# index to column
d['index1'] = d.index                   # to last column
d.reset_index(drop=True, inplace=True)  # to first column, works for Multiindex too
d.rename_axis('cool').reset_index()     # name index first

# --- Work on Rows ------------------------------------------------------------

import pandas as pd

d = pd.read_csv('data/titanic.csv')

d[d['Age'] > 35]
d[d['Age'] > 35][0:10]

# Combining multiple conditional statements, each must be surrounded by
# parentheses (). You have to use &/| instead of and/or.
d[(d.Age > 35) & (d.Sex == 'female')]  # AND
d[(d.Age > 35) * (d.Sex == 'female')]  # same
d[(d.Age > 35) | (d.Sex == 'female')]  # OR
d[(d.Age > 35) + (d.Sex == 'female')]  # same

d[d.Pclass.isin([2, 3])]       # Passengers in class 2 and 3
d[~d.Pclass.isin([2, 3])]      # Passengers not in class 2 and 3

d.query('Age > 35')                    # same as above
d.query('Age > 35 & Sex == "female"')
d.query('Pclass.isin([2, 3])')
d.query('~Pclass.isin([2, 3])')

# work with NAs
d[d.Age.notna()]  # omit rows with Age==NaN
d[d.Age.isna()]  # select rows with Age==NaN
d[d.Age.isnull()]  # same, isnull() is just an alias for isna()

d[d.notna().all(axis=1)]  # omit rows with any NaN
d[d.isna().all(axis=1)]  # [], rows all NAs
d[d.isna().sum(axis=1) > 1]  # rows with more than one NA

# work with duplicates
d.duplicated()
d.drop_duplicates()
d.drop_duplicates(subset='calories')

# --- Select specific rows and columns ---

# [] is not sufficiant!, needs loc/iloc
# d.loc[,] for using column names, row labels or a condition expression.
#          On both sides of the comma, you can use a single label, a list
#          of labels, a slice of labels, a conditional expression or a colon.
d.loc[d.Age > 25, 'Name']
d.loc[d.Age > 25, ['Name', 'Sex']]
d.loc[100:105, 'Pclass':'Sex']  # Here, 100:105 are 'str' indexes '100' to '105'.

# d.iloc[,] for using position in the table.
d.iloc[9:25, 2:5]

# With loc/iloc nes values can be assigned:
d.iloc[0:3, 3] = "anonymous"

# get and set index (rownames)
df.index
df.set_index('Name', inplace=True)  # Column 'Name' moved to index
df.reset_index(inplace=True)  # and back
# df.reset_index(drop=True, inplace=True)  # index not back to column

# example:
j = d.columns.get_loc("Sex")  # 4
i = d.index.get_loc(5)  # 5
d.iloc[i:i + 20:2, j - 2:j + 1]

# .at/.iat are much faster than .loc/.iloc
# for selecting a single element from a DataFrame:

d.at[2, 'Age']
d.iat[1, 2]

# --- Subsetting Multiindex DataFrame: .xs() ----------------------------------

import pandas as pd

d = pd.DataFrame({
    'variable': ['asdf', 'qwer'] * 4,
    'value': [32, 57, 32, 10, 8, 54, 56, 77]
},
    index=pd.MultiIndex.from_arrays(
        [['one', 'one', 'two', 'two'] * 2,
         ['red', 'blue'] * 4],
        names=('number', 'color')),
)

d

d.xs('one')  # default: axis=0, level=0, drop_level=True
d.xs('one', axis=0, level=0)  # same
d.xs('red', level=1)
d.xs('A', axis=1)

# more:
# https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-mi-slicers
