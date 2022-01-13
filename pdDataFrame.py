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
print('{}\n'.format(df_drop))
