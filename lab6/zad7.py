import numpy as np

macierz = np.zeros((5, 5), dtype=int)
macierz[0, 0] = 1
macierz[4, 0] = 1
macierz[0, 4] = 1
macierz[4, 4] = 1

def zamiana(macierz):
    return 1 - macierz

print(macierz)

macierz_zamieniona = zamiana(macierz)
print("\n", macierz_zamieniona)