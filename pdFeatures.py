
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
# print(x_weight)
# print(x_weight.sum(axis=1))

#Quiz
# 1. The code exercises for this chapter involves calculating various baseball statistics based on the values of other statistics. The mlb_df DataFrame is predefined, and contains all historic MLB hitting statistics.
# We also provide a col_list_sum function. This is a utility function to calculate the sum of multiple columns across a DataFrame.
# def col_list_sum(df, col_list, weights=None):
#     col_df = df[col_list]
#     if weights is not None:
#         col_df = col_df.multiply(weights)
#     return col_df.sum(axis=1)
# The mlb_df doesn't contain one of the key stats in baseball, batting average. Therefore, we'll calculate the batting average and add it as a column in mlb_df.
# mlb_df['BA'] = mlb_df['H'] / mlb_df['AB']
# CODE HERE
# # CODE HERE
# mlb_df['BA'] = mlb_df['H'] / mlb_df['AB']

# 2. Though mlb_df contains columns for doubles, triples, and home runs (labeled '2B', '3B', 'HR'), it does not contain a column for singles.
# However, we can calculate singles by subtracting doubles, triples, and home runs from the total number of hits. We'll label the singles column as '1B'.
# CODE HERE
# other_hits = col_list_sum(mlb_df, ['2B', '3B', 'HR'])
# mlb_df['1B'] = mlb_df['H'] - other_hits
# Now that mlb_df contains columns for all four types of hits, we can calculate slugging percentage (column label 'SLG'). The formula for slugging percentage is:

# SLG = ​1B+2⋅2B+3⋅3B+4⋅HR / AB
# ​​Set weighted_hits equal to col_list_sum with mlb_df as the first argument and a list of numerator column labels as the second argument. The weights keyword argument should be a list of integers from 1 to 4, inclusive.
# CODE HERE
# weighted_hits = col_list_sum(mlb_df, ['1B', '2B', '3B', 'HR'], weights=[1,2,3,4])

# 3. We can now calculate the slugging percentage by dividing the weighted sum by the number of at-bats.
# CODE HERE
# mlb_df['SLG'] = weighted_hits / mlb_df['AB']