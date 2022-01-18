import pandas as pd

# Qualitative Features
df = pd.DataFrame({
    'T1': [20, 32, 44],
    'T2': [22, 33, 12],
    'T3': [54, 77, 98]
    })

# print('{}\n'.format(df))
# print('{}\n'.format(df.sum()))
# print('{}\n'.format(df.sum(axis=1)))
# print('{}\n'.format(df.sum(axis=0)))
# print('{}\n'.format(df.mean()))
print('{}\n'.format(df.mean(axis=1)))