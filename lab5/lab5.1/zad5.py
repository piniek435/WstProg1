import random

wszystkie_liczby = list(range(1, 49))
wylosowane_kule = random.sample(wszystkie_liczby, 6)
wylosowane_kule.sort()

print(wylosowane_kule)