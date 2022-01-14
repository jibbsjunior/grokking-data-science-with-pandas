import pandas as pd

#Direct Indexing
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]}, index=['r1', 'r2'])

col1 = df["c1"]
# print('{}\n'.format(col1))

df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
# print('{}\n'.format(df))

first_two_rows = df[0:2]
# print('{}\n'.format(first_two_rows))

last_two_rows = df['r2':'r3']
# print('{}\n'.format(last_two_rows))

# There will be a KeyError when we uncomment the line 13 and run again
# df['r1']

#Other Indexing - iloc & loc
df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
# print('{}\n'.format(df.iloc[1]))
# print('{}\n'.format(df.iloc[[0, 2]]))
bool_list = [False, True, True]
# print('{}\n'.format(df.iloc[bool_list]))
# print('{}\n'.format(df.loc['r2']))
# print('{}\n'.format(df.loc[bool_list]))
single_val = df.loc['r1', 'c2']
# print('{}\n'.format(single_val))
# print('{}\n'.format(df.loc[['r1', 'r3'], 'c2']))
df.loc[['r1', 'r3'], 'c2'] = 0
# print('{}\n'.format(df))


