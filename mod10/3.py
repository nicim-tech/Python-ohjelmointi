class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin
        pass
    def siirry_kerrokseen(self, kerros):
        while self.nykyinen != kerros:
            if self.nykyinen < kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()
    def kerros_ylos(self):
        if self.nykyinen + 1 >= self.ylin:
            self.nykyinen = self.ylin
        else:
            self.nykyinen += 1
            print(f"Nykyinen kerros: {self.nykyinen}")
    def kerros_alas(self):
            if self.nykyinen - 1 <= self.alin:
                self.nykyinen = self.alin
            else:
                self.nykyinen -= 1
            print(f"Nykyinen kerros: {self.nykyinen}")
class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin, ylin))
    def aja_hissia(self, hissin_numero, kerros):
            self.hissit[hissin_numero].siirry_kerrokseen(kerros)
    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)

talo1 = Talo(1, 10, 3)
talo1.aja_hissia(0, 7)
talo1.aja_hissia(1, 5)
talo1.aja_hissia(2, 4)
talo1.palohälytys()
for i, hissi in enumerate(talo1.hissit):
    print(f"Hissi {i} on nyt kerroksessa {hissi.nykyinen}")