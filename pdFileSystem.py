from ast import With
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
# df.to_csv('data.csv', index=False)
# temp = pd.read_csv('data.csv')
# print('{}\n'.format(temp))

#excel
df = pd.DataFrame([['Ajibola Rilwan', 'Ajibola Olaide'], ['Adebayo Rilwan', 'Ajibola Olalekan'], ['Rilwan Olaide', 'Olaide AJibola']])
df1 = pd.DataFrame([['Olaide', 'AJibola'], ['Olalekan', 'Ridwan'], ['Adebayo', 'Ogidan']])
with pd.ExcelWriter('./pandas/data.xlsx') as writer:
    df.to_excel(writer, index=False, sheet_name='Jb')
    df1.to_excel(writer, index=False, sheet_name='RD')

df_read = pd.read_excel('./pandas/data.xlsx')
# print('{}\n'.format(df_read))

#json
df = pd.DataFrame([['Ajibola Rilwan', 'Ajibola Olaide'], ['Adebayo Rilwan', 'Ajibola Olalekan'], ['Rilwan Olaide', 'Olaide AJibola']])

# df.to_json('./pandas/data.json')
# df2 = pd.read_json('./pandas/data.json')

df.to_json('./pandas/data.json', orient='index')
df2 = pd.read_json('./pandas/data.json')
df2 = pd.read_json('./pandas/data.json', orient='index')

print('{}\n'.format(df2))


