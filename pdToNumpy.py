import pandas as pd
import numpy as np

df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02', 'canoro01'],
  'yearID': [2016, 2016, 2021, 2016, 2017, 2019],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA', 33],
  'BB': [12, 32, 44, 22, 14, 41],
  'HR': [21, 39, 43, 38, 39, 40
]})

converted = pd.get_dummies(df)
# print('{}\n'.format(converted.columns))
# print('{}\n'.format(converted[['teamID_BOS',
#                                'teamID_SEA']]))
# n_matrix = df.values
# print(repr(n_matrix))

#Quiz
# 1. We only want the data in df to be from the current century, so we need to first apply a filter.
# CODE HERE
# fl = df[df['yearID'] >= 2000] 
# df = fl

# 2. We also don't want any of the NaN values in our data. We can filter those out using the special dropna function.
# CODE HERE
# df = df.dropna()

# 3. Finally, we want to convert each categorical feature into a set of indicator features for each of its categories.
# CODE HERE
# df = pd.get_dummies(df)
# matrix = df.values