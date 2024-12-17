osszeg = 0
szam = None

while szam != 0 or szam != '':
    szam = int(input("Kérek egy számot: "))
    osszeg += szam 
print(f"Az osszeadott szamok osszege: {osszeg}")