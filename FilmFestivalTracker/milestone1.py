title = input("Enter film title: ")
genre = input("Enter genre: ")
capacity = int(input("Enter theatre capacity: "))
tickets_sold = int(input("Enter tickets sold: "))
ticket_price = float(input("Enter ticket price (Rs.): "))
duration = int(input("Enter duration (minutes): "))

print("\nType of tickets sold:", type(tickets_sold))
print("Type of ticket price:", type(ticket_price))

occupancy = tickets_sold / capacity * 100
vacant_seats = capacity - tickets_sold
gross_revenue = tickets_sold * ticket_price
hours = duration // 60
minutes = duration % 60

formatted_title = title.strip().title()
formatted_genre = genre.strip().upper()
screening_code = formatted_title.replace(" ", "")[:3].upper() + str(duration)[-2:]

print("\n===== SCREENING REPORT =====")
print("Film Title      :", formatted_title)
print("Genre           :", formatted_genre)
print("Capacity        :", capacity)
print("Tickets Sold    :", tickets_sold)
print("Ticket Price    : Rs.", ticket_price)
print(f"Occupancy       : {occupancy:.2f}%")
print("Vacant Seats    :", vacant_seats)
print(f"Gross Revenue   : Rs.{gross_revenue:.2f}")
print(f"Duration        : {hours} hr {minutes} min")
print("Screening Code  :", screening_code)
