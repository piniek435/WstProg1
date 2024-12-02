# a.
imie = input("Podaj imię: ")
print(f"Witaj {imie}")

# b.
wiek = input("Podaj wiek: ")
print(f"Twój wiek to: {wiek}")

# c.
imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
inicjaly = f"{imie[0]}.{nazwisko[0]}."
print(inicjaly)

# d.
lancuch = input("Podaj łańcuch: ")
print(lancuch * 5)

# e.
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polaczony_lancuch = lancuch1 + lancuch2
print(polaczony_lancuch)

# f.
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polowa_lancucha = (lancuch1 + lancuch2)[:len(lancuch1 + lancuch2)//2]
print(polowa_lancucha)