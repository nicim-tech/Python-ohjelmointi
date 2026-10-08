import json
import os

# Ladataan peli
def Lataapeli(nimi):
    try:
        with open(f"tallennus_{nimi}.json", "r") as tiedosto:
             return json.load(tiedosto)
    except FileNotFoundError:
         print("Tallennettua peliä ei löytynyt")
         return None
# Tallennetaan peli
def tallenna_peli(pelaaja):
    tallennus = {"nimi": pelaaja.nimi, "sijainti": pelaaja.sijainti, "ekologisuus": pelaaja.ekologisuus, "tavarat": pelaaja.tavarat}
    with open(f"tallennus_{pelaaja.nimi}.json", "w", encoding="utf-8") as tiedosto:
         json.dump(tallennus, tiedosto, ensure_ascii=False, indent=4)
    with open(f"tallennus_{pelaaja.nimi}.json", "r") as tiedosto:
         dataluettu = json.load(tiedosto)
    print("")
    print("Peli tallennettu onnistuneesti. ")
    print("")

# Tallennuksen tietojen näyttäminen 
def Printtaatallennetuttiedostot(dataluettu): 
    print("") 
    print("~ TALLENNETTU PELI ~") 
    print(f"Pelaaja: {dataluettu['nimi']}") 
    print(f"Sijainti: {dataluettu['sijainti']}") 
    print(f"Ekologisuus: {dataluettu['ekologisuus']}") 
    print(f"Tavarat: {dataluettu['tavarat']}") 
    print(f"Kynsimuoto: {dataluettu['kynsimuoto']}") 
    print(f"Väri: {dataluettu['vari']}") 
    print(f"Koristelu: {dataluettu['koristelu']}") 
    print("")

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
        self.ekologisuus = 5
        self.kynsimuoto = None
        self.koristelu = None
        self.vari = None
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
    def lataa_tiedot(self, dataluettu):
        self.nimi = dataluettu["nimi"]
        self.sijainti = dataluettu["sijainti"]
        self.ekologisuus = dataluettu["ekologisuus"]
        self.tavarat = dataluettu["tavarat"]
        self.kynsimuoto = dataluettu["kynsimuoto"]
        self.vari = dataluettu["vari"]
        self.koristelu = dataluettu["koristelu"]
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
    def lista1(nimi):
        print("")
        print("~ KYNNENMUOTO ~")
        print("Coffin kynnet")
        print("Ballerina kynnet")
        print("Almond kynnet")
        print("Stiletto kynnet")
        print("")
        choice = input("Valitse ensin kynsillesi muoto 1-4: ")
        if choice == "1":
            nimi.kynsimuoto = "Coffin"
            print("Kestävä valinta <3: kynsien huolellinen hoito vähentää turhaa materiaalien käyttöä.")
            nimi.ekologisuus += 8
        elif choice == "2":
            nimi.kynsimuoto = "Ballerina"
            print("Materiaaleja kuluu enemmän ja jätettä syntyy enemmän.")
            nimi.ekologisuus -= 3
        elif choice == "3":
            nimi.kynsimuoto = "Almond"
            print("Kestävä valinta <3: Käytetään materiaaleja säästeliäästi ja vältetään turhaa jätettä.")
            nimi.ekologisuus += 5
        elif choice == "4":
            nimi.kynsimuoto = "Stiletto"
            print("Kynnet menivät rikki, teknikko aloittaa alusta ja joutuu avaamaan uuden paketin")
            nimi.ekologisuus -= 6
        else:
            print("Virheellinen valinta")
            return
    def lista3(nimi):
        print("")
        print("~ VÄRI ~")
        print("Vaaleanpunainen glitter")
        print("Luonnonvihreä")
        print("Oranssi")
        print("Valkoinen")
        print("")
        choice = input ("Valitse kynsillesi väri 1-4: ")
        if choice == "1":
            nimi.vari = "Vaaleanpunainen glitter"
            nimi.ekologisuus -= 3
            print("Glitteriä kului paljon ja osa materiaalista jäi käyttämättä.")
        elif choice == "2":
            nimi.vari = "Luonnonvihreä"
            nimi.ekologisuus += 4
            print("Kestävä valinta: Valitsit ekologisen sävyn ja vähän materiaalia kuluttavan värin.")
        elif choice == "3":
            nimi.vari = "Oranssi"
            nimi.ekologisuus -= 5
            print("Käytit liikaa materiaalia...")
        elif choice == "4":
            nimi.vari = "Valkoinen"
            print("Kestävä valinta <3: Värin käyttö oli säästeliästä!")
            nimi.ekologisuus += 6
        else:
            print("Virheellinen valinta")
            return
        print("")
        print(f"Valitsit väriksi: {nimi.vari}")
        print(f"Ekologisuuspisteesi: {nimi.ekologisuus}")
    def valikko():
         print("~ PÄÄVALIKKO ~")
         print("Aloita peli kirjoittamalla 1")
         print("Avaa inventaario kirjoittamalla 2")
         print("Näät creditit kirjoittamalla 3")
         print("Näe pelaajan tiedot kirjoittamalla 4")
         print("Tallenna peli kirjoittamalla 5")
         print("Lataa peli kirjoittamalla 6")
         print("Lopeta peli kirjoittamalla, <lopeta> 7")
         print("")
    def lista2(nimi):
         print("")
         print("~ KORISTELUVAIHTOEHDOT ~")
         print("valinta 1, pelkkä pohja väri")
         print("valinta 2, french tip")
         print("valinta 3, base + koristeet")
         print("valinta 4, animal print")
         print("")
         choice = input("Valitse seuraavaksi koristeluvaihtoehto 1-4: ")
         if choice == "1":
             nimi.koristelu = "Pohjaväri"
             print("Valitsit pelkän pohjavärin.")
             print("Kestävä valinta<3: koristeluun ei mene ylimääräisiä materiaaleja")
             nimi.ekologisuus += 6
         elif choice == "2":
             nimi.koristelu = "french tip"
             print("Valitsit french tip koristelun")
             print("Hieno ja kohtuullisen vähämateriaalinen koristelu.")
             nimi.ekologisuus += 3
         elif choice == "3":
             nimi.koristelu = "base + koristeet"
             print("Valitsit base + koristeet")
             print("Koristeita käytetään enemmän ja materiaalia kuluu enemmän.")
             nimi.ekologisuus -= 3
         elif choice == "4":
             nimi.koristelu = "animal print"
             print("Valitsit animal print koristelun")
             print("Koristeluun tarvitaan useita eri materiaaleja.")
             nimi.ekologisuus -= 5
         else:
            print("Virheellinen valinta.")
            return
         print("")
         print(f"Valitsit koristeluksi: {nimi.koristelu}")
         print(f"Ekologisuuspisteesi: {nimi.ekologisuus}")

    def show_inventory(tavarat):
        print("")
        print("~ INVENTAARIO ~")
        if len(tavarat) == 0:
            print("Inventaario on tyhjä.")
        else:
            for tavara in tavarat:
                print(f"- {tavara}")
    print("")

inventaario = []

def studio1(nimi):
    print("")
    print("Astut aulaan sisälle ja istut, sillä edessäsi on vielä muutama muu asiakas. Aula on siistin näköinen, mutta asiakaspalvelija näyttää hermostuneelta")
    print("Jatkat omia ajatuksiasi ja odotat kärsivällisesti. ")
    print("")

    choice = input("Olet aulassa odottamassa vuoroasi, sinulle tarjotaan vettä hyväksytkö vaikka se on muovisessa pullossa? (kyllä/ei): ")
    if choice == "kyllä":
        nimi.lisaa_tavara("Vesipullo")
        nimi.ekologisuus -= 4
        print("Otat vesipullon vastaan")
    elif choice == "ei":
        nimi.ekologisuus += 4
        print("Kieltäydyt vedestä")
    else:
        print("Et vastannut oikein")
    print("")
    print(f"Ekologisuuspisteesi: {nimi.ekologisuus}")
    print("")
    print("On sinun vuorosi ja istut alas pehmeälle tuolille")
    Kynsistudio.lista1(nimi)
    print("")
    print("Valitaan kynsiesi väri!")
    input("Paina Enter jatkaaksesi kynsien väriin")
    Kynsistudio.lista3(nimi)
    print("")
    input("Paina Enter jatkaaksesi kynsien koristeluun...")
    Kynsistudio.lista2(nimi)
    print(f"Kynsimuoto: {nimi.kynsimuoto}")
    print(f"Koristelu: {nimi.koristelu}")
    print("")
    print(f"Ekologisuuspisteesi: {nimi.ekologisuus}")
    print("")

    print("Kyntesi ovat valmiit!")
    print(" ~ KYNSIEN LOPPUTULOS ~")
    print(f"Muoto: {nimi.kynsimuoto}")
    print(f"Väri: {nimi.väri}")
    print(f"Koristelu: {nimi.koristelu}")
    print(f"Ekologisuus pisteet {nimi.ekologisuus}")
    print("\nPELIN LOPPUTULOS")
    if nimi.ekologisuus >= 30:
        print("VOITIT PELIN!")
        print("Kynsistä tuli upeat ja onnistuit tekemään erittäin ekologisia valintoja.")
    elif nimi.ekologisuus >= 15:
        print("Hienosti tehty!")
        print("Kynnet onnistuivat, mutta olisit voinut tehdä vielä ekologisempia valintoja.")
    else:
        print("Et voittanut tällä kertaa.")
        print("Materiaalien kulutus oli liian suurta.")
# Luodaan nimi hahmo
nimi = Pelaaja(name)

while True:

    Kynsistudio.valikko()

    valinta = input("Valitse toiminto: ").lower()

    if valinta == "1":
        print("")
        input("Paina Enter päästäksesi eteenpäin...")
        studio1(nimi)

    elif valinta == "2":
        print("")
        print("Avasit inventaarion.")
        Kynsistudio.show_inventory(nimi.tavarat)

    elif valinta == "3":
        print("")
        print("~ CREDITS ~")
        print("Pelin suunnittelija ja ohjelmoija: Nicim ")
        print("Tehty vuonna: 2026")

    elif valinta == "4":
        nimi.nayta_tiedot()

    elif valinta == "5":
        tallenna_peli(nimi)
    elif valinta == "6":
        print("")
        print("~ LADATAAN PELI ~")

        tallennettu = Lataapeli(pelaaja.nimi)

        if tallennettu is not None:
        pelaaja.lataa_tiedot(tallennettu)
        print("Peli ladattu onnistuneesti!")
        pelaaja.nayta_tiedot()        

    elif valinta == "7" or valinta == "lopeta":
        print("")
        print("Peli lopetettu.")
        break

    else:
        print("Virheellinen valinta. Valitse numero 1-6.")