def averages(luvut):
    avg = sum(luvut) / len(luvut)
    return avg
lista = [1.3, 2.5, 3.9, 4.2, 5.1]
keskiarvo = averages(lista)
print(f"Keskiarvo : {keskiarvo:.2f}")

def average_grade(luvut):
    keskiarvot = []
    for alkio in luvut:
        keskiarvo = averages(alkio)
        keskiarvot.append(keskiarvo)

        return keskiarvot

lista = [[1.3, 2.5, 3.9, 4.2, 5.1, 6.7, 7.8, 8.9, 9.0]]
keskiarvot = average_grade(lista)

for keskiarvo in keskiarvot:
    print(f"Keskiarvo: {keskiarvo:.2f}")
