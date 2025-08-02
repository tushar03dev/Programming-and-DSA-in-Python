items = ['Mango','Apple','Banana','Orange','Apple']

unique_items = set()
for item in items:
    if item in unique_items:
        print("Duplicate ", item)
        break
    else:
        unique_items.add(item)