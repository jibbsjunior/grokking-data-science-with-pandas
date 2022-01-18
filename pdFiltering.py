from traceback import print_tb
import pandas as pd
import numpy as np

#Filter Condition
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02', 'canoro01'],
  'yearID': [2016, 2016, 2016, 2016, 2017, 2019],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA', np.nan],
  'HR': [31, 39, 43, 38, 39, 40
]})

# print('{}\n'.format(df))
cruzne02 = df['playerID'] == 'cruzne02'
# print(cruzne02)
hr40 = df['HR'] > 40
# print('{}\n'.format(hr40))

teamBOS = df['teamID'] != 'BOS'
# print('{}\n'.format(teamBOS))

#Filter from functions
str_f1 = df['playerID'].str.startswith('c')
# print('{}\n'.format(str_f1))
str_f2 = df['playerID'].str.endswith('2')
# print('{}\n'.format(str_f2))
str_f3 = ~df['playerID'].str.contains('o')
# print('{}\n'.format(str_f3))

#isin function
isin_f1 = df['playerID'].isin(['cruzne02', 'canoro01'])
# print('{}\n'.format(isin_f1))

isin_f2 = df['yearID'].isin([2015, 2017])
# print('{}\n'.format(isin_f2))

isna = df['teamID'].isna()
# print('{}\n'.format(isna))

isnotna = df['teamID'].notna()
# print('{}\n'.format(isnotna))
