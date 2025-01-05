import numpy as np

macierz = np.random.randint(0, 100, (5, 5))
print(macierz)

print("Największy element:", macierz.max())
print("Najmniejszy element:", macierz.min())
print("Największe elementy w wierszach:", macierz.max(axis=1))
print("Największe elementy w kolumnach:", macierz.max(axis=0))
print("Suma wartości w wierszach:", macierz.sum(axis=1))