while True :
    nimi = input("Mikä on nimesi? ")
    ika = int(input("Anna ikäsi: "))
    if ika < 12:
        print("Et ole tarpeeksi vanha pelaamaan tätä peliä.")
        break
    print(f"hei {nimi}, tervetuloa pelaamaan peliä!")
    print(f"Olet {ika} vuotta vanha, joten voit pelata peliä.")
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
        print("Jokaisella kortillansa on oma arvonsa, ja sinun tehtäväsi on kerätä suurin kortti, vältä jokereita sillä ne miinustavat sinulta pisteitä. Ässät antavat sinulle lisää mahdollisuuksia ottaa uusia kortteja vaihtamalla yhden korteistasi pakkaan, jos kuitenkin saat jokerin tiput takaisin alkuun. 2 on hyödylinen kortti, sillä se pelastaa sinut jos osut jokeriin.")
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
        elif valinta == "2":
                print("Ohjeet: Tässä pelissä sinun täytyy kerätä suurin kortti voittaaksesi ja välttää jokereita, jotka vievät sinut takaisin alkuun. Onnea peliin!")
        elif valinta == "3":
            print("Avasin credits-ikkunan:")
            credits()
        elif valinta == "lopeta":
            print("Lopetetaan peli. Kiitos pelaamisesta!")
            break
    break
            
            