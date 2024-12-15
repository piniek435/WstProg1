import pandas as pd

data = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
}
df = pd.DataFrame(data)

# a
df_ocena_wyzsza = df[df['Ocena'] > 4]
print("a) Studenci z oceną > 4:\n", df_ocena_wyzsza)

# b
df_posortowany_wiek = df.sort_values(by='Wiek')
print("\nb) Studenci posortowani według wieku:\n", df_posortowany_wiek)

# c
df_srednia_wiek = df.groupby('Ocena')['Wiek'].mean().reset_index()
print("\nc) Średnia wieku dla każdej oceny:\n", df_srednia_wiek)

# d
data_poprawa = {
    'Nr_albumu': [2, 4, 5],
    'Ocena_Poprawa': [4.0, 4.5, 3.5]
}
df_poprawa = pd.DataFrame(data_poprawa)

df_polaczone = pd.merge(df, df_poprawa, on='Nr_albumu', how='left')
print("\nd) Połączenie z ocenami z poprawy:\n", df_polaczone)

# e
df.to_csv('studenci.csv', index=False)
print("\ne) Zapisano do pliku studenci.csv")

# f
df_wczytany = pd.read_csv('studenci.csv')
print("\nf) Wczytany DataFrame:\n", df_wczytany)

if df.equals(df_wczytany):
    print("\nf) Wczytanie przebiegło poprawnie, DataFrames są identyczne.")
else:
    print("\nf) Wczytanie nie powiodło się, DataFrames są różne.")

# g
nowy_student = {'Nr_albumu': 6, 'Imię': 'Jan', 'Nazwisko': 'Kowalski', 'Ocena': 4.0, 'Wiek': 22}
df = pd.concat([df, pd.DataFrame([nowy_student])], ignore_index=True)
print("\ng) DataFrame po dodaniu nowego studenta:\n", df)

# h
unikalne_oceny = df['Ocena'].unique()
print("\nh) Unikalne oceny:\n", unikalne_oceny)

# i
liczba_ocena_5 = df[df['Ocena'] == 5].shape[0]
print("\ni) Liczba studentów z oceną 5:", liczba_ocena_5)