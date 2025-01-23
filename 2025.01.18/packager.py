def package(items: list[int], limit: int) -> list[list[int]]:
    
    items = items.copy()
    boxes: list[list[int]] = []
    box: list[int] = []

    while len(items) > 0:

        if sum(box) + items[0] <= limit:
            box.append(items[0])
            items.pop(0)
        else:
            boxes.append(box)
            box = []

    return boxes