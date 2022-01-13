from operator import index
import pandas as pd
import numpy as np

#Dataframe
df = pd.DataFrame()
# print('{}\n'.format(df))

df = pd.DataFrame([3, 4])
# print('{}\n'.format(df))

df = pd.DataFrame([[2, 4]])
# print('{}'.format(df))

df = pd.DataFrame([[2, 4], [2, 4]], index=['r1', 'r2'], columns=['c1', 'c2'])
# print('{}\n'.format(df))

df = pd.DataFrame({'c1': [2, 3], 'c2': [4, 5]}, index=['r1', 'r2'])
# print('{}\n'.format(df))

#upcasting
upcast = pd.DataFrame([[2, 4], [3.2, 5]])
# print('{}\n'.format(upcast))
# print("upcast types: \n %s", upcast.dtypes)

#appending
df = pd.DataFrame([[1, 3], [4, 5]])
ser = pd.Series([2, 1], name='r3')

df_app = df.append(ser)
# print('{}\n'.format(df_app))

df_app = df.append(ser, ignore_index=True)
# print('{}\n'.format(df_app))
df2 = pd.DataFrame([[2, 4], [9, 8]])
df_app = df.append(df2)
# print('{}\n'.format(df_app))

#Dropping data
df = pd.DataFrame([{'c1': [1, 3], 'c2': [4, 2], 'c3': [3, 8]}], index=['r1', 'r2', 'r3'])

#drop row1
df_drop = df.drop(labels='r1')

df_drop = df.drop(labels=['c1', 'c3'], axis=1)

df_drop = df.drop(index='r2')

df_drop = df.drop(columns='c2')

df.drop(index='r2', columns='c2')
# print('{}\n'.format(df_drop))

# #Quiz
# 1. The coding exercise for this chapter involves creating various pandas DataFrame objects.
# We'll first create a DataFrame from a Python dictionary. The dictionary will have key-value pairs 'c1':[0, 1, 2, 3] and 'c2':[5, 6, 7, 8], in that order.
# The index for the DataFrame will come from the list of row labels ['r1', 'r2', 'r3', 'r4'].
# Set df equal to pd.DataFrame with the specified dictionary as the first argument and the list of row labels as the index keyword argument.
df = pd.DataFrame({'c1': [0, 1, 2, 3], 'c2': [5, 6, 7, 8]}, index=['r1', 'r2', 'r3', 'r4'])
# print('{}\n'.format(df))

# 2. We'll create another DataFrame, this one representing a single row. Rather than a dictionary for the first argument, we use a list of lists, and manually set the column labels to ['c1, 'c2'].
# Since there is only one row, the row labels will be ['r5'].
row_df = pd.DataFrame([[9, 9]], columns=['c1', 'c2'], index=['r5'])

# 3. After creating row_df, we append it to the end of df and drop row 'r2'.
df_app = df.append(row_df)
df_drop = df_app.drop(labels='r2')
