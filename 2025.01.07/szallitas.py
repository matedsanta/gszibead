def line_to_list(items_line):
    items: list[int] = []
    temp: str
    for char in items_line:
        if char not in [",", " "]:
            temp += char
        else:
            items.append(int(temp))
            temp = ""

try:
    with open("tomeg.txt", "r") as file:
        items_line = file.readline()
        line_to_list(items_line)
except FileNotFoundError:
    items: list[int] = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]

def sum(sumlist: list[int]) -> int:
    count = 0
    if sumlist.__len__() == 0: return 0
    for item in sumlist:
        count += item
    return count

print(f"2. feladat\nA tárgyak össztömege: {sum(items)} kg")
boxes: list[list[int]] = []
while items.__len__() > 0:
    
    box: list[int] = []
    while (sum(box) + items[0]) <= 20:
        box.append(items[0])
        items.pop(0)
        if items.__len__() == 0: 
            boxes.append(box)
            break
    else:
        boxes.append(box)
    
print("3.feladat\nA dobozok tartalmának tömege (kg): ", end="")
for db in boxes:
    print(sum(db), end=" ")
print() # Sortörés
print(f"A szükséges dobozok száma: {boxes.__len__()}")