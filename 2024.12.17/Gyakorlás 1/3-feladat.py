from math import sqrt

valid = False
while not valid:
    bekert = input("Írjon be egy számot: ")
    try:
        szam = int(bekert)
        valid = True
    except ValueError:
        print("Kérlek egy számot írj be!")

print(f"Kerekitett gyok: {round(sqrt(szam))} ")



    