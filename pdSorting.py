import pandas as pd

#Sorting by feature
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02', 'canoro01'],
  'yearID': [2016, 2016, 2021, 2016, 2017, 2019],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA', 33],
  'HR': [21, 39, 43, 38, 39, 40
]})

sort1 = df.sort_values('yearID')
# print('{}\n'.format(sort1))

sort2 = df.sort_values('playerID', ascending=False)
# print('{}\n'.format(sort2))

sort3 = df.sort_values(['yearID', 'playerID'] ,ascending=[True, False])
# print('{}\n'.format(sort3))

sort4 = df.sort_values(['yearID', 'HR'],
                       ascending=[True, False])
# print('{}\n'.format(sort4))