
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
# print('{}\n'.format(df.mean(axis=1)))

#Weighted Features
x = pd.DataFrame({
    'P1': [1.2, 0.4, 9.3],
    'P2': [2.1, 2.3, 4.3],
    'P3': [3.2, 3.5, 5.5]
})

# print('{}\n'.format(x))
# print('{}\n'.format(x.multiply(2)))
# print('{}\n'.format([1000, 1], axis=0))
# x_milliseconds = x.multiply([1000, 1], axis=0)
# print('{}\n'.format(x_milliseconds)) #not working
x_weight = x.multiply([1, 0.5, 2])
print(x_weight)
print(x_weight.sum(axis=1))