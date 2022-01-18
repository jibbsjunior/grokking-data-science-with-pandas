from traceback import print_tb
import pandas as pd
import numpy as np

#Filter Condition
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02', 'canoro01'],
  'yearID': [2016, 2016, 2016, 2016, 2017, 2019],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA', np.nan],
  'HR': [21, 39, 43, 38, 39, 40
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

#Feature Filtering
hr40_df = df[df['HR'] > 40]
# print('{}\n'.format(hr40_df))

nothr30_hf = df[~(df['HR'] > 30)]
# print('{}\n'.format(nothr30_hf))

#Quiz
# 1. We'll first filter mlb_df for the top MLB hitting seasons in history, which we define as having a batting average above .300.
# CODE HERE
# top_hitters = mlb_df[mlb_df['BA'] > .300]

# 2. Next we filter for the players whose player ID does not start with the letter a.
# CODE HERE
# exclude_a = mlb_df[~mlb_df['playerID'].str.startswith('a')]

# 3. We'll now retrieve the statistics for two specific players. Their player IDs are 'bondsba01' and 'troutmi01'.
# CODE HERE
# two_ids = ['bondsba01', 'troutmi01']
# two_players = mlb_df[mlb_df['playerID'].isin(two_ids)]