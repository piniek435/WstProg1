litera = input("Podaj literę: ")
if litera.isalpha() and len(litera) == 1:
    if litera.isupper():
        print("Wielka litera")
    else:
        print("Mała litera")
else:
    print("To nie jest litera")