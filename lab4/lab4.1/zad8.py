stopnie = ("Szeregowy", "Kapral", "Sierżancie", "Porucznik", "Kapitan", "Major", "Pułkownik")

ilosc_stopni = len(stopnie)
major_index = stopnie.index("Major")
pulkownik_wstepowanie = "Pułkownik" in stopnie

print(ilosc_stopni)
print(major_index)
print(pulkownik_wstepowanie)