
import pandas as pd

# date time: .dt accessor
s = pd.Series(pd.date_range("20130101 09:10:12", periods=4))
s.dt.hour
s.dt.second
s.dt.day
s.dt.year

s[s.dt.day == 2]  # selecting

s.dt.tz_localize("UTC").dt.tz_convert("US/Eastern")  # tz transformation

s.dt.strftime("%Y/%m/%d")  # formatting

# convert dataframe column to datetime
d = pd.DataFrame({'year': [1980,1982,1973,1999],
                  'pop': [72,54,92,77],
                  'crime': [20,44,39,57]})
d.year = pd.to_datetime(d.year, format='%Y')
d.dtypes

# sum by Decade
d.insert(0, 'Decade', d.index.year - d.index.year%10)
d.groupby('Decade').sum()

# same with .resample
d.set_index('year', inplace=True)
d.resample('10AS').sum()  # not the same

