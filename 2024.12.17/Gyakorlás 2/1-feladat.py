import re
pattern = re.compile(r"^[1-9]\d{3}$")

ev = 0
while not pattern.match(str(ev)):
    ev = input("Milyen évet írunk?: ")

szul_ev = 0
while not pattern.match(str(szul_ev)):
    szul_ev = input("Milyen évben született?: ")

ev = int(ev)
szul_ev = int(szul_ev)

kulonbseg = ev - szul_ev

if kulonbseg > 0:
    print(f"Ön {kulonbseg} éves!")
elif kulonbseg < 0:
    print(f"Negatív érték({kulonbseg})! Ellenőrizze az évszámokat!")
else:
    print(f"Az érték 0! Ellenőrizze az évszámokat!")