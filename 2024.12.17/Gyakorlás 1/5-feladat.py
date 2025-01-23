szo = input("Írj be egy szót: ")
szo = szo.lower()
sorrend = ''
betulista = sorted(szo)
for char in betulista:
    sorrend += char


print(sorrend)