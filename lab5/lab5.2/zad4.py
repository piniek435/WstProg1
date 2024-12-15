import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
}
df = pd.DataFrame(data)

# a
df_pensja_wyzsza = df[df['Pensja'] > 5000]
print("a) Pracownicy z pensją > 5000 PLN:\n", df_pensja_wyzsza)

# b
df_posortowany_wiek = df.sort_values(by='Wiek')
print("\nb) Pracownicy posortowani według wieku:\n", df_posortowany_wiek)

# c
df_srednia_pensja = df.groupby('Stanowisko')['Pensja'].mean().reset_index()
print("\nc) Średnia pensja dla każdego stanowiska:\n", df_srednia_pensja)

# d
data_zmiana_stanowiska = {
    'ID': [2, 4, 5],
    'Nowe_Stanowisko': ['Starszy Programista', 'Starszy Programista', 'Dyrektor']
}
df_zmiana = pd.DataFrame(data_zmiana_stanowiska)

df_polaczone = pd.merge(df, df_zmiana, on='ID', how='left')
print("\nd) Połączenie z informacją o zmianie stanowisk:\n", df_polaczone)

# e
df.to_csv('pracownicy.csv', index=False)
print("\ne) Zapisano do pliku pracownicy.csv")

# f
df_wczytany = pd.read_csv('pracownicy.csv')
print("\nf) Wczytany DataFrame:\n", df_wczytany)

if df.equals(df_wczytany):
    print("\nf) Wczytanie przebiegło poprawnie")
else:
     print("\nf) Wczytanie nie przebiegło poprawnie")