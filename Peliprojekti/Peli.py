while True:
    nimi = input("Mikä on nimesi? ")
    ika = int(input("Anna ikäsi: "))
    if ika < 12:
        print("Et ole tarpeeksi vanha pelaamaan tätä peliä.")
        break
 # Peli alkaa valitsemalla valikosta 1. Pelaa peliä
    print(f"hei nimi {nimi}, tervetuloa pelaamaan peliä!")
    print(f"Olet {ika} vuotta vanha, joten voit pelata peliä.")
    def valikko():
        print(f"päävalikko")
        print(f"Aloita peli: 1. Pelaa peliä")
        print(f"Katso ohjeet: 2. Katso ohjeet")
        print(f"Lopeta peli: 3. Kirjoita 'lopeta' lopettaaksesi pelin")
        print ("")
    while True:
        print("")
        valikko()
        valinta = input("Valitse vaihtoehto: ")
        if valinta == "1":
            print("Aloitetaan peli!")
        elif valinta == "2":
                print("Ohjeet: Tässä pelissä sinun täytyy kerätä suurin kortti voittaaksesi ja välttää jokereita, jotka vievät sinut takaisin alkuun. Onnea peliin!")
        elif valinta == "3":
            print("Avasit lopeta peli.")
        elif valinta == "lopeta":
            print("Lopetetaan peli. Kiitos pelaamisesta!")
            break
            
            