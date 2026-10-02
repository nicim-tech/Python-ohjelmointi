nimi1 = input("Anna nimesi: ")
nimi2 = input("Anna toinen nimi: ")
nimi3 = input("Anna kolmas nimi: ")
pisteet1 = input("Anna pisteesi: ")
pisteet2 = input("Anna pisteesi: ")
pisteet3 = input("Anna pisteesi: ")

opiskelijat = {"nimi1": {pisteet1}, "nimi2": {pisteet2}, "nimi3": {pisteet3}}

def pisteet():
    if pisteet < 50:
        print("Hylätty")
    elif pisteet >= 50 and pisteet <= 59:
        print("Arvosana 1")