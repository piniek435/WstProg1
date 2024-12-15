import f_mat

# Sposób a
wynik_kwadrat_a = f_mat.kwadrat(10)
wynik_szescian_a = f_mat.szescian(3)
wynik_dodaj_a = f_mat.dodaj(10, 5)

print(wynik_kwadrat_a)
print(wynik_szescian_a)
print(wynik_dodaj_a)

# Sposób b
from f_mat import kwadrat, szescian, dodaj

wynik_kwadrat_b = kwadrat(10)
wynik_szescian_b = szescian(3)
wynik_dodaj_b = dodaj(10, 5)

print(wynik_kwadrat_b)
print(wynik_szescian_b)
print(wynik_dodaj_b)