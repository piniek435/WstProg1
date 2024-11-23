znalezione = []
liczba = 2
licznik = 0

while licznik < 10:
    pierwsza = True
    i = 2
    while i * i <= liczba:
        if liczba % i == 0:
            pierwsza = False
            break
        i += 1
    if pierwsza:
        znalezione.append(str(liczba))
        licznik += 1
    liczba += 1

print(",".join(znalezione))