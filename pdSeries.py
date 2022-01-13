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
# print('{}\n'.format(series))

#Dictionary input
series = pd.Series({'a': 1, 'b': 2, 'c': 3})
# print('{}\n'.format(series))

#Quiz
# 1. The first Series we create will contain basic floating point numbers. The list we use to initialize the Series is [1, 3, 5.2].
s1 = pd.Series([1, 3, 5.2])

# 2. The second Series we create comes from performing elemental multiplication on s1 using a separate list of floating point numbers.
s2 = pd.Series(s1 * [0.1, 0.2, 0.3])

# 3. We'll create another Series, this time with integers. The list we use to initialize this Series is [1, 3, 8, np.nan]. This Series will also have row labels, which will be ['a', 'b', 'c', 'd'].
s3 = pd.Series({'a': 1, 'b': 3, 'c': 8, 'd': np.nan})

# 4. The final Series we create will be initialized from a Python dictionary. The dictionary will have key-value pairs 'a':0, 'b':1, and 'c':2.
s4 = pd.Series([0, 1, 2], index=['a', 'b', 'c'])
