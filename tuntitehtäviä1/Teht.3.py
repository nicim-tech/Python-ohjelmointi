kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))
pinta_ala = kanta * korkeus
piiri = 2 * (kanta + korkeus)
print(f"Pinta-ala on: {pinta_ala}")
print(f"Piiri on: {piiri}")

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
luku3 = float(input("Anna kolmas luku: "))
print(f"Lukujen summa on: {luku1 + luku2 + luku3}")
print(f"Lukujen tulo on: {luku1 * luku2 * luku3}")
print(f"Lukujen keskiarvo on: {(luku1 + luku2 + luku3) / 3}")

import random
# 1. Arvotaan  kolme satunnaislukua väliltä 0-9 ja tulostetaan se.
satunnaisluku1 = random.randint(0, 9)
satunnaisluku2 = random.randint(0, 9)
satunnaisluku3 = random.randint(0, 9)
print(f"Kolmenumeroinen koodi: {satunnaisluku1}{satunnaisluku2}{satunnaisluku3}")
#2. Arvotaan neljä satunnaislukua väliltä 1-6 ja tulostetaan se.
satunnaisluku4 = random.randint(1,6)
satunnaisluku5 = random.randint(1,6)
satunnaisluku6 = random.randint(1,6)
satunnaisluku7 = random.randint(1,6)
print(f"Neljänumeroinen koodi: {satunnaisluku4}{satunnaisluku5}{satunnaisluku6}{satunnaisluku7}")