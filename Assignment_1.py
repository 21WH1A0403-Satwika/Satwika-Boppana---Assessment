inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]

total = 0
low_stock = []
cat_rev = {}

for item in inventory:
    name, cat, price, sold, left = item
    rev = price * sold
    total += rev
    if left < 5:
        low_stock.append(name)
    cat_rev[cat] = cat_rev.get(cat, 0) + rev

print("Total Revenue:", total)
print("Low Stock Items:", low_stock)
print("Category Revenue:", cat_rev)
