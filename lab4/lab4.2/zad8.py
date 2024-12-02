# A.
def wyswietlanie_parametrow(*args):
    for arg in args:
        print(arg)

wyswietlanie_parametrow(1, 2, 8, 9)

# B.
def znajdowanie_maksimum(*args):
    if not args:
        return None
    maksimum = args[0]
    for arg in args:
        if arg > maksimum:
            maksimum = arg
    return maksimum

maks = znajdowanie_maksimum(1, 2, 8, 9)
print(maks)
