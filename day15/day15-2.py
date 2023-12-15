from collections import OrderedDict


def remove_item(boxes, box_hash, label):
    if not box_hash in boxes:
        return
    box = boxes[box_hash]
    if not label in box:
        return
    del box[label]


def add_item(boxes, focal_length, box_hash, label):
    if box_hash in boxes:
        box = boxes[box_hash]
        box[label] = focal_length
    else:
        new_dict = OrderedDict()
        new_dict[label] = focal_length
        boxes[box_hash] = new_dict


def calculate_focusing_power(boxes):
    power = 0
    for box_nb, box in boxes.items():
        for i, box_item in enumerate(box.items()):
            focal_length = box_item[1]
            power += (box_nb + 1) * (i + 1) * int(focal_length)
    return power


def parse(text):
    boxes = {}
    for step in text.split(","):
        # for key, val in step.split("="):

        if "=" in step:
            operation = "="
        else:
            operation = "-"

        label, focal_length = step.split(operation)
        box_hash = 0
        for c in label:
            box_hash += ord(c)
            box_hash *= 17
            box_hash %= 256

        if operation == "=":
            add_item(boxes, focal_length, box_hash, label)

        if operation == "-":
            remove_item(boxes, box_hash, label)

    return calculate_focusing_power(boxes)


with open("day15.txt", 'r') as f:
    text = f.read()

    total = parse(text)

    print(f"Day 15-1: {total}")
