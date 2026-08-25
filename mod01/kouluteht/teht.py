pituus = float(input("Anna kuhan pituus (cm): "))
if pituus < 37:
    print("Kuha on alamittainen.")
    print(f"Kuha on {37 - pituus} cm alimmasta sallitusta pyyntimitasta.")
    print("Heitä kuha takaisin järveen")
else:
    print("Kuha on tarpeeksi suuri.")
    print("Voit ottaa kuhan mukaasi.")