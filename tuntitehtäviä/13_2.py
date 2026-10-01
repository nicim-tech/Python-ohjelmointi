try:
    luku1 = int(input("Anna numero: "))
    luku2 = int(input("Anna toinen numero: "))
    print(luku1 / luku2)
except ValueError:
    print("Virhe: syötetty arvo ei ole kokonaisluku.")

except ZeroDivisionError:
    print("Virhe: Nollalla ei voi jakaa:(")
print("Ohjelman suoritus jatkuu.")