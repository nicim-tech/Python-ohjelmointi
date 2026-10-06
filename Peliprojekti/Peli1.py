
def lue_tiedosto(tiedostonimi):
    with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
        return tiedosto.read()
print(lue_tiedosto("intro.txt"))
print()
print(lue_tiedosto("ohjeet.txt"))
print()

nimi = input("Anna pelaajan nimi: ")
sijainti = "alku"
pisteet = 0

print()
print("Tervetuloa peliin, {nimi}!")
print("Peli alkaa nyt")

while True:
    komento = input("\nMitä haluat tehdä? ").lower()

    if komento == "tallenna":
        with open("tallennus.txt", "w", encoding="utf-8") as tiedosto:
                  tiedosto.write(nimi + "\n")
                  tiedosto.write(sijainti + "\n")
                  tiedosto.write(str(pisteet)+ "\n")
        print("Peli tallennettu!")

    elif komento == "lopeta":
         print("Peli lopetetaan")
         break
    else:
         print("Tuntematon komento")
         print("Voit kirjoittaa tallenna, tallentaaksesi tai lopeta, lopettaaksesi pelin")



class Kynsistudio:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.inventaario = []
#Inventaario
    def lisaa_tavara(self, tavara):
        self.inventaario.append(tavara)
        print(f"Lisättiin inventaarioon: {tavara}")