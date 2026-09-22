class Julkaisut:
    julkaisujen_maara = 0

    def __init__(self, julkaisunimi, julkaisija):
        Julkaisut.julkaisujen_maara = Julkaisut.julkaisujen_maara + 1
        self.julkaisunumero = Julkaisut.julkaisujen_maara
        self.julkaisunimi = julkaisunimi
        self.julkaisija = julkaisija

    def tulosta_tiedot(self):
        print(f"{self.julkaisunumero}: {self.julkaisunimi} ({self.julkaisija})")

class sivut(Julkaisut):
    def __init__(self, julkaisunimi, julkaisija, sivumaara):
        self.sivumaara = sivumaara
        super().__init__(julkaisunimi, julkaisija)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"sivumaara: {self.sivumaara}")

julkaisut = []
julkaisut.append(Julkaisut("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(sivut("Hytti n:o6", "Rosa Liksom", 200))

for t in julkaisut:
    t.tulosta_tiedot()