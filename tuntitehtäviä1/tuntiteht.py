opintopisteet = input("Anna opintopisteiden määrä: ")
if int(opintopisteet) >= 150:
    print("Olet suorittanut riittävästi opintopisteitä.")

sää = input("Anna säätila: ")
if sää == "lämmin" and sää != "pilvinen":
    print("Sää on lämmin ja ei pilvinen.")

kalankoko = input("Anna kalan koko (cm): ")
kalanika = input("Anna kalan ikä (vuosia): ")
if int(kalankoko) > 10 and int(kalankoko) <= 65 and int(kalanika) >= 10:
    print("Kalan koko on sallittu.")