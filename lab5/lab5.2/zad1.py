import pandas as pd

na_values = ['NA', 'n/a', 'NaN']
df = pd.read_csv('demografia.csv', decimal='.', na_values=na_values)
print(df)
