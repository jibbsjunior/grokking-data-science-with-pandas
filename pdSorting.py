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

#Quiz
# 1. We'll sort yearly_stats_df using two different methods. The first method sorts by 'yearID' in ascending order.
# CODE HERE
# by_year = yearly_stats_df.sort_values('yearID')

# 2. The next sorting method will sort by 'HR' in descending order.
# CODE HERE
# best_hr = yearly_stats_df.sort_values('HR', ascending=False)

# 3. The final sorting method will again sort yearly_stats_df by 'HR' in descending order, but this time we break ties with 'SO' in ascending order.
# CODE HERE
# best_hr_so = yearly_stats_df.sort_values(['HR', 'SO'], ascending=[False, True])