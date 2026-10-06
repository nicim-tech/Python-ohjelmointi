
# Importataan random randint, jotta pakasta voi nostaa kortteja.
import random

# Määritetään korkeimman kortin pelaaminen ja pisteiden tulos >

def pelaa_korkein_kortti():
    pakka, kortti_arvot = korttiPakka()

    pelaaja_tulos = 0
    tietokone_tulos = 0

    print()
    print("Korkein kortti Voittaa!")
    print()

#Pelataan kolme kierrosta

    for kierros in range(1, 4):
        print(f"\n--- Kierros {kierros} ---")

#Pelaaja saa satunnaisen kortin pakasta

    pelaaja_kortti = random.choice(pakka)
    pakka.remove(pelaaja_kortti)

#tietokone saa satunnaisen kortin pakasta

    tietokoneen_kortti = random.choice(pakka)
    pakka.remove(tietokoneen_kortti)

# Tulostetaan kortit

    print(f"Sinun korttisi: {pelaaja_kortti}")
    print(f"Tietokoneen kortti: {tietokoneen_kortti}")

    p_arvo = kortin_arvo(pelaaja_kortti, kortti_arvot)
    t_arvo = kortin_arvo(tietokoneen_kortti, kortti_arvot)

    
# Tulostetaan myös kortin arvo

    print(f"Sinun korttisi arvo: {p_arvo}")
    print(f"Tietokoneen kortin arvo: {t_arvo}")

# Määritetään kortin arvo hierarkia

    if p_arvo > t_arvo:
        print("Voitit tämän kierroksen!")
        pelaaja_tulos += 1
    elif p_arvo < t_arvo:
        print("Tietokone voittaa tämän kierroksen")
        tietokone_tulos += 1
    else:
        print("Tasapeli!")
    print(f"Tulos -> Sinä: {pelaaja_tulos} Tietokone: {tietokone_tulos}")


    print()
    print("---LOPPUTULOS---")
    print(f"Sinä: {pelaaja_tulos}")
    print(f"Tietokone: {tietokone_tulos}")
    if pelaaja_tulos > tietokone_tulos:
        print("Sinä voitit pelin!")
    elif pelaaja_tulos < tietokone_tulos:
        print("Tietokone voitti pelin!")
    else:
        print("Peli päättyi tasan!")

# Määritetään kortin arvo >

def kortin_arvo(kortti, kortti_arvot):
    kortin_nimi = kortti.split()[-1]
    return kortti_arvot[kortin_nimi]

def uusi_kierros(self, nosta_kortti):
     print("Pelataan uusi kierros!")
     nosta_kortti = random.choice

# Tehdään luokka pelaaja >

class Player:
    def __init__(self, nimi):
         self.nimi = nimi
         self.kortit = []
         self.pisteet = 0

# Rakennetaan pakka, joka sisältää 52 korttia. >

def korttiPakka():
    maat = ["Ruutu","Hertta", "Risti", "Pata"]
    kortti_arvot = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
    pakka = []
    for maa in maat:
        for kortti in kortti_arvot:
            pakka.append(f"{maa} {kortti}")
    return pakka, kortti_arvot

# valikko >

def valikko():
        print("# päävalikko")
        print("Aloita peli painamalla 1")
        print("Katso ohjeet painamalla 2")
        print("Katso credits painamalla 3")
        print("Kirjoita 'lopeta' lopettaaksesi pelin")

# creditit >

def credits():
        print("Credits: Tämä peli on kehitetty ja suunniteltu Nicim 2026.")


def lista():
        nici = []
        print("Tässä on lista korteista:")
        while True:
            kortit = input("Nosta kortti pakasta: ")
            if kortit == "lopeta":
                print("Lopetetaan peli. Kiitos pelaamisesta!")
                break
            nici.append(kortit)
        return nici
def inventaario(kortit):
        for item in kortit:
            print(f"- {item}")

# Tehdään pelin aloitus valikko + printataan ohjeet peliin

#Tehdään valikko, ohjelma kysyy nimen ja iän pelaajalta. >
while True :
    nimi = input("Mikä on nimesi? ")
    try:
        ika = int(input("Anna ikäsi: "))
    except ValueError:
         print("Anna ikä numerona.")
         continue
    if ika < 12:
        print("Et ole tarpeeksi vanha pelaamaan tätä peliä.")
        break
    print(f"hei {nimi}, oletko valmis pelaamaan peliä?")
    print(f"Olet {ika} vuotta vanha, joten olet tarpeeksi vanha pelatakasesi peliä.")
    break

#PÄÄOHJELMA --> 

while True:
    print("")
    valikko()
    valinta = input("Valitse toiminto:" )
    if valinta == "1":
        print("Aloitetaan peli!")
        pelaa_korkein_kortti()
    elif valinta == "2":
        print()
        print("OHJEET")
        print("Sinä ja tietokone saatte kortin.")
        print("Korkeamman kortin saanut voittaa kierroksen.")
        print("Peli pelataan 3 kierrosta.")
        print("Se, joka voittaa enemmän kierroksia, voittaa pelin.")
    elif valinta == "3":
        credits()
    elif valinta == "lopeta":
        print("Lopetetaan peli. Kiitos pelaamisesta!")
        break
    else:
        print("Virheellinen valinta.")
        break