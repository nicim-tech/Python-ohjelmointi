import json
import os

# Ladataan peli
def Lataapeli(nimi):
    try:
        with open(f"tallennus_{nimi}.json", "r") as tiedosto:
             return json.load(tiedosto)
    except FileNotFoundError:
         return None
# Tallennetaan peli
def tallenna_peli(pelaaja):
    tavaroidenNimet = []
    for tavara in pelaaja.tavarat:
        tavaroidenNimet.append(tavara.nimi)

    tallennus = {"nimi": pelaaja.nimi, "sijainti": pelaaja.sijainti.nimi, "ekologisuus": pelaaja.ekologisuus, "tavarat": pelaaja.tavarat}
    with open(f"tallennus_{pelaaja.nimi}.json", "w") as tiedosto:
         json.dump(tallennus, tiedosto)
    with open(f"tallennus_{pelaaja.nimi}.json", "r") as tiedosto:
         dataluettu = json.load(tiedosto)
# Printtaa ilman "#" merkkiä
#Printtaatallennetuttiedostot(dataluettu)

# Funktio print komennolle
def Printtaatallennetuttiedostot(dataluettu):
     print(f"Pelaaja: {dataluettu["nimi"]}, Sijainti: {dataluettu["sijainti"]}, Ekologisuus: {dataluettu["ekologisuus"]}, Tavarat: {dataluettu["tavarat"]}")

# Kansio pelille
kansio = r"C:\Users\nicim\Python ohjelmointi\Peliprojekti"
# Lukee kansion tiedostosta
def Luetideosto(tiedostonimi):
    polku = os.path.join(kansio, tiedostonimi)
    try:
        with open(polku, "r", encoding="utf-8") as tiedosto:
            return tiedosto.read()
    except FileNotFoundError:
        return(f"Tiedostoa {polku} ei löytynyt. ")
# Kysyy nimen ja iän käyttäjältä
print("")
name = input("Mikä nimesi on?: ")
print("")
print("Hei", name, "!")
print("")
age = int(input("Kuinka vanha olet?: "))
if age < 12:
    print("Et ole tarpeeksi vanha pelaamaan tätä peliä :(")
else:
    print("Tervetuloa pelaamaan kynsistudiota", name, "!")
    print("")

#Pelaaja class
class Pelaaja():
    def __init__(self, nimi):
        self.nimi = nimi
        self.tavarat = []
        self.sijainti = "Aula"
        self.ekologisuus = 0
    def lisaa_tavara(self, tavara):
        self.tavarat.append(tavara)
        print(f"Sait tavaran: {tavara}")
    def nayta_tiedot(self):
        print("")
        print(f"Nimi: {self.nimi}")
        print(f"Sijainti: {self.sijainti}")
        print(f"Ekologisuus: {self.ekologisuus}")
        print(f"Tavarat: {self.tavarat}")
        print("")

## Kynsistudio -->

class Kynsistudio:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.inventaario = []
#Inventaario
    def lisaa_tavara(self, tavara):
        self.inventaario.append(tavara)
        print(f"Lisättiin inventaarioon: {tavara}")
#Lista
    def lista1():
        print("")
        print("~ KYNNENMUOTO ~")
        print("Coffin kynnet")
        print("Ballerina kynnet")
        print("Almond kynnet")
        print("Stiletto kynnet")
        print("")
    def valikko():
         print("~ PÄÄVALIKKO ~")
         print("Aloita peli kirjoittamalla 1")
         print("Avaa inventaario kirjoittamalla 2")
         print("Näät creditit kirjoittamalla 3")
         print("Näe pelaajan tiedot kirjoittamalla 4")
         print("Tallenna peli kirjoittamalla 5")
         print("Lopeta peli kirjoittamalla, <lopeta> 6")
         print("")
    def lista2():
         print("")
         print("~ KORISTELUVAIHTOEHDOT ~")
         print("valinta 1, pelkkä pohja väri")
         print("valinta 2, french tip")
         print("valinta 3, base + koristeet")
         print("valinta 4, animal print")
    def show_inventory(tavarat):
        print("")
        print("~ INVENTAARIO ~")

        if not tavarat:
            print("Inventaario on tyhjä.")
        else:
            for tavara in tavarat:
                print(f"- {tavara}")
        print("")

    def credits():
         print("")
         print("~ CREDITS ~")
         print("Pelin suunnittelija ja ohjelmoija: Nicim ")
         print("Tehty vuonna: 2026")
    def studiot():
         print("Base")
         print("Viilaus")
         print("Koristeet")

inventaario = []

def studio1(pelaaja):
    print("")
    print("Astut aulaan sisälle ja istut, sillä edessäsi on vielä muutama muu asiakas. Aula on siistin näköinen, mutta asiakaspalvelija näyttää hermostuneelta")
    print("Jatkat omia ajatuksiasi ja odotat kärsivällisesti. ")
    print("")

    choice = input("Olet aulassa odottamassa vuoroasi, sinulle tarjotaan vettä hyväksytkö vaikka se on muovisessa pullossa? (kyllä/ei): ")
    if choice == "kyllä":
        pelaaja.lisaa_tavara("Vesipullo")
        print("Otat vesipullon vastaan, ekologisuus - 4")
    elif choice == "ei":
        pelaaja.ekologisuus += 4
        print("Kieltäydyt vedestä, ekologisuus + 4")
    else:
        print("Et vastannut oikein")

    print("")
    print(f"Ekologisuuspisteesi: {pelaaja.ekologisuus}")
    print("")

# Pelin alkutiedot



# Luodaan pelaaja hahmo
pelaaja = Pelaaja(name)

while True:

    Kynsistudio.valikko()

    valinta = input("Valitse toiminto: ").lower()

    if valinta == "1":
        print("")
        input("Paina Enter päästäksesi eteenpäin...")
        studio1(pelaaja)

    elif valinta == "2":
        print("")
        print("Avasit inventaarion.")
        Kynsistudio.show_inventory(pelaaja.tavarat)

    elif valinta == "3":
        Kynsistudio.credits()

    elif valinta == "4":
        pelaaja.nayta_tiedot()

    elif valinta == "5":
        tallenna_peli(pelaaja)

    elif valinta == "6" or valinta == "lopeta":
        print("")
        print("Peli lopetettu.")
        break

    else:
        print("Virheellinen valinta. Valitse numero 1–6.")