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
print('{}\n'.format(df_app))