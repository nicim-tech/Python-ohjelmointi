print("Terve, pelaaja!")
nimi = input("Mikä on nimesi?")
print(f"Oletko valmis pelaamaan {nimi}?")
print(" Tarkistetaan vielä ikäsi!")
ika = int(input("Anna ikäsi: "))
if ika < 12:
    print("Et ole tarpeeksi vanha pelaamaan tätä peliä.")
    exit()
else:
    print("Hienoa, aloitetaan!")
valikko = input("Valitse valikosta: 1. Pelaa peliä, 2. Katso ohjeet, 3. Lopeta peli: ")
if valikko == "1":
    print("Aloitetaan peli!")
    # Peli alkaa valitsemalla valikosta 1. Pelaa peliä
if valikko == "2": 
    print("Ohjeet pelin aloittamiseen: Tässä pelissä sinun tulee pelata ja kerätä erityisiä esineitä. Varo jokereita ja kerää pisteitä! Onnea peliin!")
if valikko == "3":
    print("Kiitos pelaamisesta! Nähdään seuraavalla kerralla.")
    exit()
