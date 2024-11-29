# 1.
imie = input("Podaj imię: ")
print(f"Witaj {imie}")

# 2.
wiek = input("Podaj wiek: ")
print(f"Twój wiek to: {wiek}")

# 3.
imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
inicjaly = f"{imie[0]}.{nazwisko[0]}."
print(inicjaly)

# 4.
lancuch = input("Podaj łańcuch: ")
print(lancuch * 5)

# 5.
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polaczony_lancuch = lancuch1 + lancuch2
print(polaczony_lancuch)

# 6.
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polowa_lancucha = (lancuch1 + lancuch2)[:len(lancuch1 + lancuch2)//2]
print(polowa_lancucha)