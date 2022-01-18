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
print('{}\n'.format(metrics2))