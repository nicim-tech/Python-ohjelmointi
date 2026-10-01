
data = "Pelaaja1 voitti pelin"
with open("../Peliprojekti/tallennus/save.txt", "w") as tiedosto:
    tiedosto.write(data)
print("Tiedostoon kirjoitettu", data)

with open("../Peliprojekti/tallennus/save.txt", "w") as tiedosto: