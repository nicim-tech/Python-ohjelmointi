print("Terve, pelaaja!")
nimi = input("Mikä on nimesi?")
print(f"Oletko valmis pelaamaan {nimi}?")
print(" Tarkistetaan vielä ikäsi!")
ika = int(input("Anna ikäsi: "))
if ika < 10:
    print("Et ole tarpeeksi vanha pelaamaan tätä peliä, mutta voit silti yrittää!")
print("Aloitetaan!")