with open('notowania.txt', 'r') as plik:
    for linia in plik:
        print(linia.strip())

f = open("notowania.txt", "a")
f.write("\nALR, 113")
f.close()

with open('notowania.txt', 'r') as plik:
    for linia in plik:
        print(linia.strip())