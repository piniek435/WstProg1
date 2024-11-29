while True:
    try:
        liczba = int(input("Podaj liczbę całkowitą: "))
        if liczba < 0:
            break
    except ValueError:
        print("To nie jest liczba")