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

#Quiz
# 1. The coding exercises for this chapter involve directly indexing into a predefined DataFrame, df.
# We'll initially use direct indexing to get the first column of df as well as the first two rows.
col_1 = df['c1']
row_12 = df[0:2]

# 2. Next, we'll use iloc to retrieve the first and third rows of df.
# CODE HERE
row_13 = df.iloc[[0, 2]]

# 3. Finally, we use loc to set each value of the second column, in the third and fourth rows, equal to 12. The row key we use for indexing will be ['r3','r4'], while the column key will be 'c2'.
# CODE HERE
df.loc[['r3', 'r4'], 'c2'] = 12


