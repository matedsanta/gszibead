from random import randint

a = randint(1, 100)
b = randint(1, 100)

print(f"A nagyobb szám: {(a if a > b else b) if not a == b else 0 }")
