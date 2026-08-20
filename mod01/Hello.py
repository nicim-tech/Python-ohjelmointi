print("Hei, Nici!")
name = input("Mikä on nimesi? ")
print("Terve, " + name + "!")
import math
# 1 radius = float(input("Anna ympyrän säde: "))
# Kysy säde käyttäjältä ja laske ympyrän pinta-ala ja kehän pituus.
radius = float(input("Anna ympyrän säde: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"Ympyrän pinta-ala on: {area}")
print(f"Ympyrän ympärysmitta on: {circumference}")
