import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#verifying matplotlib installation
# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()


#Basics
df = pd.DataFrame({
  'playerID': ['bettsmo01', 'canoro01', 'cruzne02', 'ortizda01', 'cruzne02', 'canoro01'],
  'yearID': [2016, 2016, 2021, 2016, 2017, 2019],
  'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA', 33],
  'BB': [12, 32, 44, 22, 14, 41],
  'HR': [21, 39, 43, 38, 39, 40
]})

# df.plot(kind='line',x='yearID',y='HR')
# plt.show()
# plt.savefig('pandas/basics.png')
# df.plot(kind='line',x='yearID',y='HR')
# plt.title('HR vs. Year')
# plt.xlabel('Year')
# plt.ylabel('HR Count')
# plt.show()

#Other plots
# df.plot(kind='bar',y='HR')
# plt.ylabel('Frequency')
# plt.show()
# df.plot(kind='box',y='HR')
# plt.show()

#Multiple Features
# gca stands for 'get current axis'
ax = plt.gca()

# df.plot(kind='line',x='yearID',y='HR',ax=ax)
# df.plot(kind='line',x='yearID',y='BB', color='red', ax=ax)
# plt.show()

# df.plot(kind='box')
# plt.show()
