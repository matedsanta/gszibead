szam = int(input("Írjon be egy természetes számot: ")) + 12
(sorszam, csillagok) = (1, 1)
while sorszam < szam:
    print(" " * (szam - sorszam) + ("*" * csillagok))
    sorszam, csillagok = sorszam + 1, csillagok + 2
