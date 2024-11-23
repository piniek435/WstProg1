ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
budynki = 5
mieszkania = 10

adresy = []

for ulica in ulice:
    for budynek in range(1, budynki + 1):
        for mieszkanie in range(1, mieszkania + 1):
            adres = f"{ulica} {budynek}/{mieszkanie}"
            adresy.append(adres)

for adres in adresy:
    print(adres)