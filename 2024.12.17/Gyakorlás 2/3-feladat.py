hegyek = []
magassagok = []
for i in range(3):
    nev = input("Írja be a hegy nevét: ")
    magassag = int(input(f"Írja be a {nev} magasságát: "))
    hegyek.append(nev)
    magassagok.append(magassag)

legmagasabb = 0
legmagasabb_index = 0
for i in range(len(magassagok)):
    if magassagok[i] > legmagasabb:
        legmagasabb = magassagok[i]
        legmagasabb_index = i

print(
    f"A legmagasabb hegy a {hegyek[legmagasabb_index]}, a magassága {magassagok[legmagasabb_index]}m"
)
