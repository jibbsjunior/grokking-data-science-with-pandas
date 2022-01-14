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
print('{}\n'.format(concat))