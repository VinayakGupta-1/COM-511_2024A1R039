orders =[
    ("Order-A",45),
    ("Order-B",30),
    ("Order-C",60),
    ("Order-D",75)
]

sorted_orders = sorted(orders, key=lambda x: x[1])

print("Orders sorted by delivery time:")

for order_name,minutes in sorted_orders:
    print(f"{order_name}: {minutes} minutes")