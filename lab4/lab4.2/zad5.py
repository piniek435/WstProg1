def kalkulator_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    if bmi < 18.5:
        kategoria = "Niedowaga"
    elif 18.5 <= bmi < 24.9:
        kategoria = "Pożądana masa ciała"
    elif 25 <= bmi < 29.9:
        kategoria = "Nadwaga"
    elif 30 <= bmi < 34.9:
        kategoria = "Otyłość I stopnia"
    elif 35 <= bmi < 39.9:
        kategoria = "Otyłość II stopnia"
    else:
        kategoria = "Otyłość III stopnia"

    return bmi, kategoria


waga = 70
wzrost = 1.70
bmi, kategoria = kalkulator_bmi(waga, wzrost)
print(f"BMI: {bmi}, Kategoria: {kategoria}")
