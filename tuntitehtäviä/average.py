def average(eka, toka):
    ns = (eka + toka) / 2
    return ns

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
#keskiarvo = (luku1 + luku2) / 2
result = average(luku1, luku2)
print(f"Lukujen {luku1:.2f} ja {luku2:.2f} keskiarvo on: {result}")