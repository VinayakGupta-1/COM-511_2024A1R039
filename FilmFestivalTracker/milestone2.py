films = {
    "The Last Signal": {"genre": "Sci-Fi", "capacity": 120, "price": 150},
    "Silent Valley": {"genre": "Drama", "capacity": 80, "price": 120},
    "Laugh Track": {"genre": "Comedy", "capacity": 100, "price": 100},
    "Dark Corridor": {"genre": "Horror", "capacity": 60, "price": 130},
}

records = []
genres = set()

print("Available films:", ", ".join(films))

while True:
    title = input("\nEnter film title (or DONE to finish): ").strip()
    if title.upper() == "DONE":
        break

    if title not in films:
        print("Rejected: Unknown film.")
        continue

    capacity = films[title]["capacity"]
    sold_text = input("Enter tickets sold: ").strip()
    if not sold_text.isdigit() or int(sold_text) > capacity:
        print(f"Rejected: Tickets sold must be between 0 and {capacity}.")
        continue
    sold = int(sold_text)

    rating_text = input("Enter rating (1-5): ").strip()
    if not rating_text.isdigit() or not 1 <= int(rating_text) <= 5:
        print("Rejected: Rating must be between 1 and 5.")
        continue
    rating = int(rating_text)

    occupancy = sold / capacity * 100
    if occupancy == 100:
        status = "FULL"
    elif occupancy >= 80:
        status = "HIGH"
    elif occupancy >= 50:
        status = "GOOD"
    else:
        status = "LOW"

    record = {}
    record["title"] = title
    record["genre"] = films[title]["genre"]
    record["sold"] = sold
    record["rating"] = rating
    record["occupancy"] = occupancy
    record["status"] = status
    records.append(record)
    genres.add(films[title]["genre"])
    print("Screening recorded.")

print("\n===== DAY SUMMARY =====")
for record in records:
    print(f"{record['title']:<16} | {record['genre']:<7} | Sold: {record['sold']:<4} | "
          f"Rating: {record['rating']} | Occupancy: {record['occupancy']:.2f}% | {record['status']}")

print("\nUnique genres:", genres)

if records:
    highest = records[0]
    for record in records:
        if record["occupancy"] > highest["occupancy"]:
            highest = record
    print(f"Highest occupancy: {highest['title']} ({highest['occupancy']:.2f}%, {highest['status']})")
else:
    print("No valid screenings recorded.")
