import packager

# We initialize all lists that we'll need.
items: list[int] = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]
boxes: list[list[int]] = []
box: list[int] = []

print(packager.package(items, 20))

# While there are any items left
while len(items) > 0:
    # If the box and the next item doesn't exceed the limit..
    if sum(box) + items[0] <= 20:
        # ..then we add it to the box and remove it from the remaining items.
        box.append(items[0])
        items.pop(0)
    else:
        # ..if it does, we add the current box to all boxes and clear it for the next items.
        boxes.append(box)
        box = []

# At last, we print out the boxes.
print(boxes)


