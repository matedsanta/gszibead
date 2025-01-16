from random import choice

hats = [choice([True, False]) for f in range(7)]



for i in range(0, hats.__len__() -1):
    hats.pop(0)
    print(f"I see {hats.count(True)} white hats!")