def n_fibonacciego(n):
    if n <= 0:
        return "Liczba mniejsza od 1"
    elif n == 1 or n == 2:
        return 1
    else:
        return n_fibonacciego(n - 1) + n_fibonacciego(n - 2)

print(n_fibonacciego(8))
print(n_fibonacciego(3))
print(n_fibonacciego(-1))
