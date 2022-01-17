from operator import index
import pandas as pd

#csv
# df = pd.read_csv('./pandas/dummy.csv')

# df = pd.read_csv('./pandas/dummy.csv', index_col=0)

# df = pd.read_csv('./pandas/dummy.csv', index_col=1)
# # print('{}\n'.format(df))

# #excel
# df = pd.read_excel('./pandas/excel_dummy.xlsx')

# df = pd.read_excel('./pandas/excel_dummy.xlsx', sheet_name=None)
# # print('{}\n'.format(df))

# #json
# df = pd.read_json('./pandas/dummy.json')

# df = pd.read_json('./pandas/dummy.json', orient=index)
# print('{}\n'.format(df))


#writing to files - csv
df = pd.DataFrame([['Adebayo AJibola', 'Adegbenro Mariam', 'Stephen Akpovino'], ['Lanre Kuye', 'Big Abbass']])
df.to_csv()
print('{}\n'.format(df))