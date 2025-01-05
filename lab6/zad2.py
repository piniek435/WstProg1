import matplotlib.pyplot as plt

kategorie = ['Obuwie', 'Buty', 'Spodnie', 'Koszulki', 'Sukienki']
sprzedaz = [900, 800, 600, 700, 500]

plt.pie(sprzedaz, labels=kategorie)
plt.title('Udział kategorii w sprzedaży')
plt.show()