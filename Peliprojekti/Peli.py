print("Terve, pelaaja!")
nimi = input("Mikä on nimesi?")
print(f"Hei {nimi} Tarkistetaan vielä ikäsi!")
ika = int(input("Anna ikäsi: "))
if ika < 12:
    print("Et ole tarpeeksi vanha pelaamaan tätä peliä.")
    exit()
else:
    print("Hienoa, aloitetaan!")
     # Peli alkaa valitsemalla valikosta 1. Pelaa peliä
valikko = input("Valitse valikosta: 1. Pelaa peliä, 2. Katso ohjeet, 3. Lopeta peli: ")
if valikko == "1":
    aloitus = input(f" Hei {nimi} oletko valmis pelaamaan? (kyllä/ei): ")
    # Jos pelaaja on valmis, peli alkaa. Muuten ohjelma lopetetaan.
    if aloitus == "kyllä":
        print("Hienoa, peli alkaa!")
    if aloitus == "ei":
        print("Peli lopetetaan.")
        exit()
# Jos pelaaja valitsee ohjeet, ohjelma tulostaa ohjeet ja kysyy haluaako pelaaja palata päävalikkoon.
if valikko == "2": 
    ohjeet = print("Ohjeet pelin aloittamiseen: Tässä pelissä sinun tulee pelata ja kerätä erityisiä esineitä. Varo jokereita ja kerää pisteitä! Onnea peliin!")
    print("haluatko palata päävalikkoon?")
    if input("Kyllä/Ei: ") == "Kyllä":
        valikko = input("Valitse valikosta: 1. Pelaa peliä, 2. Katso ohjeet, 3. Lopeta peli: ")
if valikko == "3":
    print("Kiitos pelaamisesta! Nähdään seuraavalla kerralla.")
    exit()
