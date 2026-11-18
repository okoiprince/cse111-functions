import math

items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

#calculate number of boxes
boxes = items / items_per_box
#computer number of boxes 
get_boxes = math.ceil(boxes)

#display details
print(f"For {items} items, packing {items_per_box} items in each box, you will need {get_boxes} boxes.")

