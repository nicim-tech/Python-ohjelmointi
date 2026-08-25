biologinen_sukupuoli = input("Anna biologinen sukupuoli (mies/nainen): ")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/dl): "))
if biologinen_sukupuoli == "mies":
    if hemoglobiini < 134: 
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini > 195:
        print("Hemoglobiiniarvo on korkea.")
    else: 
        print("Hemoglobiiniarvo on normaali.")
elif biologinen_sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")