import random
import math

dolny_przedzial = int(input("Podaj dolny zakres przedziału: "))
gorny_przedzial = int(input("Podaj górny zakres przedziału: "))

krotka_losowa = tuple(random.randint(dolny_przedzial, gorny_przedzial) for _ in range(10))

iloczyn = 1
for liczba in krotka_losowa:
    iloczyn *= liczba

srednia_geometryczna = math.pow(iloczyn, 1/len(krotka_losowa))

print("Wylosowana krotka:", krotka_losowa)
print("Średnia geometryczna:", srednia_geometryczna)