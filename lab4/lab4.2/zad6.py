import math

def pole_trojkata(a, b, c):
    try:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Niepoprawne boki trójkąta")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Niepoprawne boki trójkąta")
        s = (a + b + c) / 2
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return pole
    except ValueError as error:
        return str(error)
    except Exception as error:
        return f"Wystąpił błąd: {error}"

a, b, c = 3, 5, 7
wynik = pole_trojkata(a, b, c)
print(wynik)
