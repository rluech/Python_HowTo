# https://towardsdatascience.com/how-to-show-all-columns-rows-of-a-pandas-dataframe-c49d4507fcf

pd.get_option('display.max_columns')      # get current state 
pd.set_option('display.max_columns', 15)  # show maximal N (int) or all (None)
pd.reset_option('display.max_columns')    # reset default

pd.get_option('display.max_colwidth')
pd.set_option('display.max_colwidth', 15)         # None: show full width

pd.get_option('display.max_rows')
pd.set_option('display.max_rows', 60)  # limit the numer of rows for head()

pd.get_option('display.min_rows')
pd.set_option('display.min_rows', 6)  # for Frames with more than max_rows

pd.get_option('display.max_seq_item')  # number of items in a nested container

pd.set_option('display.precision', 3)  # number of decimals
