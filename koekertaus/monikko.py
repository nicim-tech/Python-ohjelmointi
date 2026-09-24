monikko1 = 1,2,3,4,5,6
print(monikko1[0])
print(monikko1[0:3])


monikko4 = 2, 4, 6, 8, 10
#Ensimmäisen alkion arvo
print(monikko4[0])
#Neljännen alkion arvo
print(monikko4[3:4])
#Viimeisen alkion arvo
print(monikko4[4:5])

#monikon purkaminen muuttujiin

monikko5 = 1,2,3
(eka,toka,kolmas) = monikko5

monikko6 = 4,5,6
(yksi,kaksi,kolme)= monikko6
#Monikko paluuarvona

def matematiikkaa(numero1, numero2):
    summa = numero1 + numero2
    tulo = numero1 * numero2
#Tallennetaan muuttujirn summa ja tulo arvot monikkoon ja palautetaan se
    return(summa, tulo)
(summa, tulo) = matematiikkaa(6,2)
print(summa)
print(tulo)

#Joukon luominen
joukko1 = {1,2,3}
joukko2 = set()
#Alkioiden lisääminen ja poistaminen
joukko2.add("Evana")
print(joukko2)
joukko2.remove("Evana")
print(joukko2)
joukko3 = set()
joukko3.add("Evana")
joukko3.add("Ella")
print(joukko3)
joukko3.remove("Ella")
print(joukko3)

#Sanakirja
sanakirja1 = {"Ella": }

