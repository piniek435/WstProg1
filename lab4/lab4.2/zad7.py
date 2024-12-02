def potega(a, n):
    if n == 0:
        return 1
    return a * potega(a, n - 1)

a = float(input("Liczba a: "))
n = int(input("Stopień n: "))
wynik = potega(a, n)
print(wynik)
