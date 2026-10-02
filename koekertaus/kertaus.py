## Perusfunktio

def tervehdi():
    print("moi!")

print("Päivä alkaa kahvilla")
tervehdi()
print("Sitten muut asiat")

##funktion parametrit
def tervehdi(kerrat):
    for n in range(kerrat):
        print("Hyvää päivää " + str(n+1) + ". kerran.")
    return
print("Päivä alkaa energiajuomalla")
tervehdi(3)
range(5)

def neliosumma(eka, toka):
    ns = eka**2 + toka**2
    return ns
luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
tulos = neliosumma(luku1,luku2)
print(f"{tulos:.3f}")