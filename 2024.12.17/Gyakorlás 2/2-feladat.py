from math import sqrt

def heron(a, b, c) -> float:
    s = (a+b+c)/2
    gyokalatt = s*(s-a)*(s-b)*(s-c)
    return round((sqrt(gyokalatt)),2)

for i in range(2):
    a = int(input("Adja meg az első oldalt: "))
    b = int(input("Adja meg a második oldalt: "))
    c = int(input("Adja meg a harmadik oldalt: "))
    if a+b<c or a+c<b or b+c<a:
        print("Nem szerkeszthető háromszög!")
    else:
        print("Szerkeszthető háromszög!")
        print(f"A háromszög területe: {heron(a,b,c)}")



