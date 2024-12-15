import pandas as pd

na_values = ['.', 'NA', 'n/a', 'NaN', '']

df = pd.read_csv('demografia.csv', decimal='.', na_values=na_values, sep=',')
df_numeric = df.iloc[:, 1:]

max_przyrost = df_numeric.max().max()
kolumna_max_przyrost = df_numeric.max().idxmax()
wiersz_max_przyrost = df_numeric[kolumna_max_przyrost].idxmax()

kraj_max_przyrost = df.loc[wiersz_max_przyrost, 'KRAJE']


print(f"Największy przyrost ludności: {max_przyrost}")
print(f"Rok największego przyrostu: {kolumna_max_przyrost}")
print(f"Kraj z największym przyrostem: {kraj_max_przyrost}")