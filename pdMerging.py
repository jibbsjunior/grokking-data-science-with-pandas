import pandas as pd

df1 = pd.DataFrame({'c1':[1,2], 'c2':[3,4]},
                   index=['r1','r2'])
df2 = pd.DataFrame({'c1':[5,6], 'c2':[7,8]},
                   index=['r1','r2'])
df3 = pd.DataFrame({'c1':[5,6], 'c2':[7,8]})

concat = pd.concat([df1, df2])

concat = pd.concat([df1, df2], axis=1)

concat = pd.concat([df1, df2, df3])

concat = pd.concat([df3, df1], axis=1)
# print('{}\n'.format(concat))

#Merging
mlb_df1 = pd.DataFrame({'name': ['john doe', 'al smith', 'sam black', 'john doe'],
                        'pos': ['1B', 'C', 'P', '2B'],
                        'year': [2000, 2004, 2008, 2003]})
mlb_df2 = pd.DataFrame({'name': ['john doe', 'al smith', 'jack lee'],
                        'year': [2000, 2004, 2012],
                        'rbi': [80, 100, 12]})
# print('{}\n'.format(mlb_df1))
# print('{}\n'.format(mlb_df1))
mlb_merged = pd.merge(mlb_df1, mlb_df2)
print('{}\n'.format(mlb_merged))

#Quiz
# 1. The coding exercises for this chapter involve completing small functions that take in two DataFrame objects as input.
# The first function, concat_rows will concatenate the rows of the two DataFrames.
def concat_rows(df1, df2):
  # CODE HERE
  row_concat = pd.concat(df1, df2)

  return row_concat
  pass

# 2. The next function, concat_cols will concatenate the columns of the two input DataFrames.
def concat_cols(df1, df2):
  # CODE HERE
  col_concat = pd.concat([df1, df2], axis=1)

  return col_concat
  pass

# 3. The final function, merge_dfs will merge the two input DataFrames along their columns.
def merge_dfs(df1, df2):
  # CODE HERE
  merged_df = pd.merge([df1, df2])

  return merged_df
  pass

