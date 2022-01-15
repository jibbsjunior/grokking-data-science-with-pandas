from operator import index
import pandas as pd

#csv
df = pd.read_csv('./pandas/dummy.csv')

df = pd.read_csv('./pandas/dummy.csv', index_col=0)

df = pd.read_csv('./pandas/dummy.csv', index_col=1)
# print('{}\n'.format(df))

#excel
