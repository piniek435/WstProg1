import time
paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Pozostało {paliwo} litrów paliwa")
    paliwo = paliwo - paliwo_zuzyte_na_s
    czas += 1
    time.sleep(1)

print("Koniec lotu.")