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
leiviskä = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))
kokonaisnaula = leiviskä * 20 + naula + luoti / 32 
kokonaisluoti = kokonaisnaula * 32
luoti = 13.3 / 1000
# 1. Tulostetaan kokonaiset kilogrammat ja gramman osuus.
# Yksi luoti = 13,3 grammaa; 1000 grammaa = 1 kilogramma
massa_kg = kokonaisluoti * 13.3 / 1000
print(f"Massa nykymittojen mukaan: {massa_kg:.0f} kg ja grammat {((leiviskä + naula + luoti) % 1) * 1000:.0f} g")
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