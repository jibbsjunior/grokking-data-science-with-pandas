import pandas as pd
import numpy as np

#Series
series = pd.Series(dtype='float64')
# print('{}'.format(series))

series = pd.Series(5)
# print('{}\n'.format(series))

series = pd.Series([1, 2, 3])
# print('{}\n'.format(series))

series = pd.Series([2, 2.5]) #upcasting
# print('{}\n'.format(series))

arr = np.array([1, 3, 4])
series = pd.Series(arr, dtype=np.float32)
# print('{}\n'.format(series))

series = pd.Series([[1, 2], [2, 3]])
# print('{}\n'.format(series))

#Index
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# print('{}\n'.format(series))

series = pd.Series([6, 9, 5], index=['a', 8, 9])
print('{}\n'.format(series))
