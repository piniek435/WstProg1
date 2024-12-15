import pandas as pd

na_values = ['NA', 'n/a', 'NaN']
df = pd.read_csv('demografia.csv', decimal='.', na_values=na_values, sep=',')

przyrost_2022 = df['2022']
kraj_max_przyrost = przyrost_2022.idxmax()

print(f"Kraj z największym przyrostem ludności w 2022 roku: {df.loc[kraj_max_przyrost, 'KRAJE']}")
print(f"Wartość przyrostu: {df.loc[kraj_max_przyrost, '2022']}")