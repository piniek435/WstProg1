import time

czas_sekundy = int(input("Podaj czas w sekundach: "))

while czas_sekundy > 0:
  print(f"Pozostało {czas_sekundy} sekund")
  time.sleep(1)
  czas_sekundy -= 1

print("Koniec odliczania!")