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
# with pd.ExcelWriter('./pandas/data.xlsx') as writer:
#     df.to_excel(writer, index=False, sheet_name='Jb')
#     df1.to_excel(writer, index=False, sheet_name='RD')

df_read = pd.read_excel('./pandas/data.xlsx')
# print('{}\n'.format(df_read))

#json
df = pd.DataFrame([['Ajibola Rilwan', 'Ajibola Olaide'], ['Adebayo Rilwan', 'Ajibola Olalekan'], ['Rilwan Olaide', 'Olaide AJibola']])

# df.to_json('./pandas/data.json')
# df2 = pd.read_json('./pandas/data.json')

# df.to_json('./pandas/data.json', orient='index')
# df2 = pd.read_json('./pandas/data.json')
# df2 = pd.read_json('./pandas/data.json', orient='index')

# print('{}\n'.format(df2))

# #Quiz
# 1.  The coding exercises in this chapter reading from CSV files containing baseball data, manipulating the data, then writing the resulting data into a new CSV file.

# First, we'll read from the two CSV files 'stats.csv' and 'salary.csv'. These files contain the stats and salaries, respectively, of various baseball players.
# CODE HERE
stats_df = pd.read_csv('stats.csv')
salary_df = pd.read_csv('salary.csv')

# 2. Rather than having two separate DataFrames, we want a single DataFrame that contains the yearly stats and salaries for each player. Therefore, we can just merge the stats_df and salary_df DataFrames.
# CODE HERE
df = pd.merge(stats_df, salary_df)

# 3. Finally, we write the merged DataFrame into the file named 'out.csv'. Since the original CSV files didn't label the rows, we'll make sure not to label the rows of 'out.csv'.
# CODE HERE
df.to_csv('out.csv', index=False)


