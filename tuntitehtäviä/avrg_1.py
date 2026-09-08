def averages(luvut):
    avg = sum(luvut) / len(luvut)
    return avg
lista = [1.3, 2.5, 3.9, 4.2, 5.1]
keskiarvo = averages(lista)
print(f"Keskiarvo : {keskiarvo:.2f}")