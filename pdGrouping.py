from unicodedata import name
import pandas as pd

#Grouping
df = pd.DataFrame([{'name': ['Adebayo', 'Ajibola', 'Ridwan', 'Olaide'], 'year': [2005, 2006, 2020, 2021]}])
groups = df.groupby(name)
for n, s in groups:
    print('{}\n'.format(n))