import numpy as np

macierz = np.random.randint(0, 100, size=(5, 5))
wieksze_niz_20 = macierz[macierz > 20]
liczba_wiekszych_niz_20 = len(wieksze_niz_20)
print(liczba_wiekszych_niz_20)
srednia = np.average(macierz)
print(srednia)