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
# Podane instrukcje konwertują podaną wartość na dany typ zmiennej

# Zad 2.
uczelnia = "Studiuję na WSIiZ"
print(uczelnia)

# Zad 3.
imię = 'Jan'
wiek = 20
wzrost = 178
print (f"Nazywam się {imię} i mam {wiek} lat. \nMój wzrost to {wzrost} cm.")