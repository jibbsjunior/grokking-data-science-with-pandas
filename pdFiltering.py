import pandas as pd

#Filter Condition
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02'],
  'yearID': [2016, 2016, 2016, 2016, 2017],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
  'HR': [31, 39, 43, 38, 39
]})

# print('{}\n'.format(df))
cruzne02 = df['playerID'] == 'cruzne02'
# print(cruzne02)
hr40 = df['HR'] > 40
# print('{}\n'.format(hr40))

teamBOS = df['teamID'] != 'BOS'
print('{}\n'.format(teamBOS))
