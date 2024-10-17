import random

# Zad 1. Typ wyniku działania 1+2
# 1A
a =  1+2 # <class 'int'> dodawanie
b =1 + 4.5 # <class 'float'> dodawanie
c = 3 / 2 # <class 'float'> dzielenie zmiennoprzecinkowe
d =4 / 2 # <class 'float'> dzielenie zmiennoprzecinkowe
e =3 // 2 # <class 'int'> dzielenie całkowite
f =-3 // 2 # <class 'int'> dzielenie całkowite
g =11 % 2 # <class 'int'> dzielenie modulo (reszta z dzielenia)
h =2 ** 10 # <class 'int'> potęgowanie
i =8 ** (1/3)  # <class 'float'> potęgowanie
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h),type(i))
# 1B
print(int(3.0),float(3),float("3"),str(12.4),bool(0)) # 3 3.0 3.0 12.4 False
# Podane instrukcje konwertują podaną wartość na wskazany typ danych

# Zad 2.
uczelnia = "Studiuję na WSIiZ"
print(uczelnia)

# Zad 3.
imię = 'Jan'
wiek = 20
wzrost = 178
print (f"Nazywam się {imię} i mam {wiek} lat. \nMój wzrost to {wzrost} cm.")

# Zad 4.
cena = 39.99
rabat = 0.2
przecenionyProdukt = cena * (1-rabat)
print(f"Cena produktu po obniżeniu ceny - {przecenionyProdukt:.2f} zł")

# Zad 5.
a = int(input("Długość boku a: "))
b = int(input("Długość boku b: "))
pole = a * b
obwod = 2 * (a + b)
print(f"Pole prostokąta: {pole}")
print(f"Obwód prostokąta: {obwod}")

# Zad 6.
drogaUzytkownika = int(input("Długość podróży w km: "))
spalanie = int(input("Średnie spalanie: "))
drogaLosowa = random.randint(1, 1000)
cenaPaliwa = int(input("Cena paliwa za litr: "))

zuzycie1 = (drogaUzytkownika * spalanie) / 100
koszt1 = zuzycie1 * 6.5
zuzycie2 = (drogaLosowa * spalanie) / 100
koszt2 = zuzycie2 * cenaPaliwa

# 6A
print(f"Przewidywane zużycie paliwa: {zuzycie1} litrów")
print(f"Szacowany koszt podróży: {koszt1} zł")
# 6B
print(f"Przewidywane zużycie paliwa: {zuzycie2} litrów")
print(f"Szacowany koszt podróży: {koszt2} zł")