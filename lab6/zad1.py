import matplotlib.pyplot as plt

kategorie = ['Obuwie', 'Buty', 'Spodnie', 'Koszulki', 'Sukienki']
sprzedaz = [900, 800, 600, 700, 500]

plt.bar(kategorie, sprzedaz)
plt.title('Sprzedaż według kategorii')
plt.xlabel('Kategoria produktu')
plt.ylabel('Liczba sprzedanych sztuk')
plt.show()