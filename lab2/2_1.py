punkty = float(int(input("Podaj liczbę punktów: ")))
if punkty > 80:
    print("Zaliczono w terminie 0")
elif 50 <= punkty <= 80:
    print("Możesz poprawić wynik")
elif punkty < 50:
    print("Musisz poprawić wynik")