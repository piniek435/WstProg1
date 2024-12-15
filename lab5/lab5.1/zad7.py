import datetime

data_ostatnich_laboratoriow = "2024-12-03"
data_kolokwium = datetime.date(2024, 12, 17)
data_laboratoriow = datetime.datetime.strptime(data_ostatnich_laboratoriow, "%Y-%m-%d").date()
dzisiaj = datetime.date.today()
roznica_dni_laboratoria = (dzisiaj - data_laboratoriow).days
roznica_dni_kolokwium = (data_kolokwium - dzisiaj).days

print(f"Od ostatnich laboratoriów minęło {roznica_dni_laboratoria} dni.")
print(f"Do kolokwium pozostało {roznica_dni_kolokwium} dni.")