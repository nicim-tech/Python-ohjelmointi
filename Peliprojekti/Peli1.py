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

    tallennus = {"nimi": pelaaja.nimi, "sijainti": pelaaja.sijainti, "ekologisuus": pelaaja.ekologisuus, "tavarat": pelaaja.tavarat}
    with open(f"tallennus_{pelaaja.nimi}.json", "w") as tiedosto:
         json.dump(tallennus, tiedosto)
    with open(f"tallennus_{pelaaja.nimi}.json", "r") as tiedosto:
         dataluettu = json.load(tiedosto)
# Printtaa ilman "#" merkkiä
#Printtaatallennetuttiedostot(dataluettu)

# Funktio print komennolle
def Printtaatallennetuttiedostot(dataluettu):
     print(f"Pelaaja: {dataluettu['nimi']}, Sijainti: {dataluettu['sijainti']}, Ekologisuus: {dataluettu['ekologisuus']}, Tavarat: {dataluettu['tavarat']}")

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
        self.ekologisuus = 15
        self.kynsimuoto = None
        self.koristelu = None
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
    def lista1(pelaaja):
        print("")
        print("~ KYNNENMUOTO ~")
        print("Coffin kynnet")
        print("Ballerina kynnet")
        print("Almond kynnet")
        print("Stiletto kynnet")
        print("")
        choice = input("Valitse ensin kynsillesi muoto 1-4: ")
        if choice == "1":
            pelaaja.kynsimuoto = "Coffin"
            print("Kestävä valinta <3: kynsien huolellinen hoito vähentää turhaa materiaalien käyttöä.")
            pelaaja.ekologisuus += 8
        elif choice == "2":
            pelaaja.kynsimuoto = "Ballerina"
            print("Materiaaleja kuluu enemmän ja jätettä syntyy enemmän.")
            pelaaja.ekologisuus -= 3
        elif choice == "3":
            pelaaja.kynsimuoto = "Almond"
            print("Kestävä valinta <3: Käytetään materiaaleja säästeliäästi ja vältetään turhaa jätettä.")
            pelaaja.ekologisuus += 5
        elif choice == "4":
            pelaaja.kynsimuoto = "Stiletto"
            print("Kynnet menivät rikki, teknikko aloittaa alusta ja joutuu avaamaan uuden paketin")
            pelaaja.ekologisuus -= 6
        else:
            print("Virheellinen valinta")
            return

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
         choice = input("Valitse seuraavaksi koristeluvaihtoehto 1-4: ")
         if choice == "1":
             print("Valitsit pelkän pohjavärin.")
             print("Kestävä valinta<3: koristeluun ei mene ylimääräisiä materiaaleja")
             pelaaja.ekologisuus += 6
         elif choice == "2":
             print("Valitsit french tip koristelun")
             print("Hieno ja kohtuullisen vähämateriaalinen koristelu.")
             pelaaja.ekologisuus += 3
         elif choice == "3":
             print("Valitsit base + koristeet")
             print("Koristeita käytetään enemmän ja materiaalia kuluu enemmän.")
             pelaaja.ekologisuus -= 3
         elif choice == "4":
             print("Valitsit animal print koristelun")
             print("Koristeluun tarvitaan useita eri materiaaleja.")
             pelaaja.ekologisuus -= 5
         else:
            print("Virheellinen valinta.")
            return
         print("")
         print(f"Valitsit koristeluksi: {pelaaja.koristelu}")
         print(f"Ekologisuuspisteesi: {pelaaja.ekologisuus}")

    def show_inventory(tavarat):
        print("")
        print("~ INVENTAARIO ~")
        if len(tavarat) == 0:
            print("Inventaario on tyhjä.")
        else:
            for tavara in tavarat:
                print(f"- {tavara}")
    print("")

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
        pelaaja.ekologisuus -= 4
        print("Otat vesipullon vastaan")
    elif choice == "ei":
        pelaaja.ekologisuus += 4
        print("Kieltäydyt vedestä")
    else:
        print("Et vastannut oikein")
    print("")
    print(f"Ekologisuuspisteesi: {pelaaja.ekologisuus}")
    print("")
    print("On sinun vuorosi ja istut alas pehmeälle tuolille")
    Kynsistudio.lista1(pelaaja)
    print("")
    input("Paina Enter jatkaaksesi kynsien koristeluun...")
    Kynsistudio.lista2(pelaaja)
    print(f"Kynsimuoto: {self.kynsimuoto}")
    print(f"Koristelu: {self.koristelu}")

    choice = input("Valitse ensin kynsillesi muoto 1-4: ")
    if choice == "1":
        pelaaja.kynsimuoto = "Coffin"
        print("Kestävä valinta <3: kynsien huolellinen hoito vähentää turhaa materiaalien käyttöä.")
        pelaaja.ekologisuus += 8
    elif choice == "2":
        pelaaja.kynsimuoto = "Ballerina"
        print("Materiaaleja kuluu enemmän ja jätettä syntyy enemmän.")
        pelaaja.ekologisuus -= 3
    elif choice == "3":
        pelaaja.kynsimuoto = "Almond"
        print("Kestävä valinta: Käytetään materiaaleja säästeliäästi ja vältetään turhaa jätettä.")
        pelaaja.ekologisuus += 5
    elif choice == "4":
        pelaaja.kynsimuoto = "Stiletto"
        print("Kynnet menivät rikki, teknikko aloittaa alusta ja joutuu avaamaan uuden paketin")
        pelaaja.ekologisuus -= 6
    else:
        print("Virheellinen valinta")
        return
    print(f"Valitsit muodoksi: {pelaaja.kynsimuoto}")
    print(f"Ekologisuuspisteesi: {pelaaja.ekologisuus}")

    
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
        print("")
        print("~ CREDITS ~")
        print("Pelin suunnittelija ja ohjelmoija: Nicim ")
        print("Tehty vuonna: 2026")

    elif valinta == "4":
        pelaaja.nayta_tiedot()

    elif valinta == "5":
        tallenna_peli(pelaaja)

    elif valinta == "6" or valinta == "lopeta":
        print("")
        print("Peli lopetettu.")
        break

    else:
        print("Virheellinen valinta. Valitse numero 1-6.")