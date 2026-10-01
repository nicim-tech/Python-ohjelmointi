# Rakennetaan pakka, sisältää 52 korttia
# parametrit: none
# Return values: pakka -> lista
import random


class Player:
    def __init__(self, nimi):
         self.nimi = nimi
         self.kortit = []
         self.pisteet = 0

     
def korttiPakka():
maat = ["Ruutu","Hertta", "Risti", "Pata"]
kortti_arvot = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}

pakka = []
for maa in maat:
    for kortti in kortti_arvot:
        pakka.append(f"{maa} {kortti}")
    return pakka, kortti_arvot

def kortin_arvo(kortti, kortti_arvot):
    kortin_nimi = kortti.split([-1])
    return kortti_arvot[kortin_nimi]

def pelaa_korkein_kortti():
    print()
    print("Korkein kortti Voittaa!")
    print()
pakka, kortti_arvot = korttiPakka()
pelaaja_tulos = 0
tietokone_tulos = 0

#Pelataan kolme kierrosta
for kierros in range(1, 4):
    print(f"\n--- Kierros {kierros} ---")
#Pelaaja saa satunnaisen kortin pakasta
pelaaja_kortti = random.choice(pakka)
pakka.remove(pelaaja_kortti)
#tietokone saa satunnaisen kortin pakasta
tietokoneen_kortti = random.choice(pakka)
pakka.remove(tietokoneen_kortti)

print(f"Sinun_korttisi: {pelaaja_kortti}")
print(f"Tietokoneen_kortti{tietokoneen_kortti}")

p_arvo = kortin_arvo(pelaaja_kortti, kortti_arvot)
t_arvo = kortin_arvo(tietokoneen_kortti, kortti_arvot)

print(f"Sinun korttisi arvo: {p_arvo}")
print(f"Tietokoneen kortin arvo: {t_arvo}")

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

def credits():
     print()
     print("Credits: tämä peli on kehitetty ja suunniteltu Nicim 2026.")

def valikko():
     print()
     print("#PÄÄVALIKKO")
     print("1. Aloita peli")
     print("2. Katso ohjeet")
     print("3. Katso credits")
     print("4. kirjoita lopeta - lopeta peli")

#PÄÄOHJELMA ->

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
    print(f"hei {nimi}, tervetuloa pelaamaan peliä!")
    print(f"Olet {ika} vuotta vanha, joten voit pelata peliä.")

while True:
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








    def valikko():
        print("# päävalikko")
        print("Aloita peli painamalla 1")
        print("Katso ohjeet painamalla 2")
        print("Kirjoita 'lopeta' lopettaaksesi pelin")
        print("Katso credits painamalla 3")
        print ("")
    def lista():
        nici = []
        print("Tässä on lista korteista:")
        print("1. kortti, ruutu ässä ")
        print("2. kortti, hertta 2")
        print("3. kortti, risti 3")
        print("4. kortti, pata 4")
        print("5. kortti, ruutu 5")
        print("6. kortti, hertta 6")
        print("7. kortti, risti 7")
        print("8. kortti, pata 8")
        print("9. kortti, ruutu 9")
        print("10. kortti, hertta 10")
        print("Saat valita ensimmäisen kortin, jonka haluat pelata. Muut kortit vedät pakasta.")
        print("Jokaisella kortillansa on oma arvonsa, ja sinun tehtäväsi on kerätä suurin kortti. Peli pelataan 3 korttiin asti ja se kenellä on 3 korkeampaa korttia yhteensä voittaa, vältä jokereita sillä ne varastavat sinulta kortin. Kun nostat ässän saat vaihtaa yhden korteistasi pakkaan.")
        while True:
            kortit = input("Valitse kortti (1-10): ")
            if kortit == "lopeta":
                print("Lopetetaan peli. Kiitos pelaamisesta!")
                break
            nici.append(kortit)
        return nici
    def inventaario(kortit):
        for item in kortit:
            print(f"- {item}")
    def credits():
        print("Credits: Tämä peli on kehitetty ja suunniteltu Nicim 2026.")

    while True :
        print("")  
        valikko()
        valinta = input("Valitse toiminto: ")
        if valinta == "1":
            print("Aloitetaan peli!")
            kortit = lista()
            inventaario(kortit)
        elif valinta == "2":
                print("Ohjeet: Tässä pelissä sinun täytyy kerätä suurin kortti voittaaksesi ja välttää jokereita, jotka vievät sinut takaisin alkuun. Onnea peliin!")
        elif valinta == "3":
            print("Avasin credits-ikkunan:")
            credits()
        elif valinta == "lopeta":
            print("Lopetetaan peli. Kiitos pelaamisesta!")

            break
