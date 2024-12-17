def legmagasabb(elemek: dict) -> dict:
    legmagasabb_nev = ""
    legmagasabb_mag = 0
    for elem in elemek:
        if elemek.get(elem) > legmagasabb_mag:
            legmagasabb_mag = elemek.get(elem)
            legmagasabb_nev = elem
    return {legmagasabb_nev: legmagasabb_mag}


hegyek = {}
for i in range(3):
    nev = input("Írja be a hegy nevét: ")
    magassag = int(input(f"Írja be a {nev} magasságát: "))
    hegyek.update({nev: magassag})
print(f"A legmagasabb a {legmagasabb(hegyek)}")
