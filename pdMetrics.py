import pandas as pd

# Numeric MemoryError
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02', 'canoro01'],
  'yearID': [2016, 2016, 2021, 2016, 2017, 2019],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA', 33],
  'HR': [21, 39, 43, 38, 39, 40
]})

metrics1 = df.describe()
# print('{}\n'.format(metrics1))

hr_rbi = df[['HR','yearID']]
metrics2 = hr_rbi.describe()
metrics2 = hr_rbi.describe(percentiles=[.5])
metrics2 = hr_rbi.describe(percentiles=[.1])
metrics2 = hr_rbi.describe(percentiles=[.2, .8])
# print('{}\n'.format(metrics2))

#Categorical Features
p_ids = df['playerID']
# print('{}\n'.format(p_ids.value_counts()))
# print('{}\n'.format(p_ids.value_counts(normalize=True)))
# print('{}\n'.format(p_ids.value_counts(ascending=True)))
unique_players = df['playerID'].unique()
# print('{}\n'.format(repr(unique_players)))

unique_teams = df['teamID'].unique()
# print('{}\n'.format(repr(unique_teams)))
y_ids = df['yearID']
# print('{}\n'.format(y_ids))
# print('{}\n'.format(repr(y_ids.unique())))
# print('{}\n'.format(y_ids.value_counts()))

#Quiz
# 1. First, we'll get a summary of all the statistics in player_df.
# CODE HERE
# summary_all = player_df.describe()

# 2. Next, we want to get summaries specifically for the home run totals. The first summary will contain the default metrics from describe, while the second summary will contain the 10th and 90th percentiles.
# CODE HERE
# hr_df = player_df['HR']
# summary_hr = hr_df.describe()
# low_high_10 = hr_df.describe([.1, .9])

# 3. Finally, we'll treat the 'HR' feature as a categorical variable, with each unique home run total as a separate category. We then get the frequency counts for each category.
# CODE HERE
# hr_counts = hr_df.value_counts()

