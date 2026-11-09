import festival_utils

RECORDS_FILE = "screening_records.txt"


class FestivalScreening:
    festival_name = "Jammu Independent Film Festival"

    def __init__(self, screening_id, film_title, genre, capacity, tickets_sold, ticket_price):
        self.screening_id = screening_id
        self.film_title = film_title
        self.genre = genre
        self.capacity = capacity
        self.tickets_sold = tickets_sold
        self.ticket_price = ticket_price
        self.ratings = []

    def add_rating(self, rating):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5.")
        self.ratings.append(rating)

    def occupancy_rate(self):
        return festival_utils.calculate_occupancy(self.tickets_sold, self.capacity)

    def average_rating(self):
        return festival_utils.average_rating(self.ratings)

    def ticket_revenue(self):
        return self.tickets_sold * self.ticket_price

    def rating_text(self):
        if not self.ratings:
            return "No ratings yet"
        return f"{self.average_rating():.2f}"

    def to_record(self):
        return (f"{self.screening_id}|{self.film_title}|{self.genre}|{self.capacity}|"
                f"{self.tickets_sold}|{self.occupancy_rate():.2f}|{self.rating_text()}|"
                f"{self.ticket_revenue():.2f}")

    def __str__(self):
        return (f"[{self.screening_id}] {self.film_title} ({self.genre}) | "
                f"Occupancy: {self.occupancy_rate():.2f}% | "
                f"Avg Rating: {self.rating_text()} | "
                f"Revenue: Rs.{self.ticket_revenue():.2f}")


def save_screening(screening):
    with open(RECORDS_FILE, "a") as file:
        file.write(screening.to_record() + "\n")


def display_records():
    try:
        with open(RECORDS_FILE, "r") as file:
            print("\n===== SAVED SCREENING RECORDS =====")
            print("ID | Title | Genre | Capacity | Sold | Occupancy% | Avg Rating | Revenue")
            for line in file:
                print(" | ".join(line.strip().split("|")))
    except FileNotFoundError:
        print(f"\nError: '{RECORDS_FILE}' not found. No screening history available yet.")


def file_pointer_demo():
    try:
        with open(RECORDS_FILE, "r") as file:
            print("\n===== tell() / seek() DEMO =====")
            print("Pointer at start, tell():", file.tell())
            first_line = file.readline().strip()
            print("First record:", first_line)
            print("Pointer after reading first line, tell():", file.tell())
            file.seek(0)
            print("After seek(0), tell():", file.tell())
            print("Re-read first record:", file.readline().strip())
            print("Purpose: tell() gives current byte position; seek() moves the pointer to re-read data.")
    except FileNotFoundError:
        print(f"Error: '{RECORDS_FILE}' not found for tell()/seek() demo.")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("ValueError: Please enter a valid whole number.")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("ValueError: Please enter a valid numeric value.")


def collect_screening():
    screening_id = input("Screening ID: ").strip()
    title = input("Film title: ").strip()
    genre = input("Genre: ").strip()
    capacity = read_int("Capacity: ")
    while True:
        sold = read_int("Tickets sold: ")
        if 0 <= sold <= capacity:
            break
        print(f"Invalid: tickets sold must be between 0 and {capacity}.")
    price = read_float("Ticket price (Rs.): ")
    screening = FestivalScreening(screening_id, title, genre, capacity, sold, price)

    while True:
        entry = input("Enter rating 1-5 (or DONE): ").strip()
        if entry.upper() == "DONE":
            break
        try:
            screening.add_rating(int(entry))
        except ValueError:
            print("ValueError: Rating must be a whole number between 1 and 5.")
    return screening


def debug_demo():
    print("\n===== DEBUGGING average = sum(ratings) / len(ratings) =====")
    ratings = []
    try:
        average = sum(ratings) / len(ratings)
    except ZeroDivisionError as error:
        print("Buggy code with ratings = [] ->", type(error).__name__, ":", error)

    for ratings in ([], [4, 5, 3]):
        if len(ratings) == 0:
            print(f"Corrected, ratings = {ratings} -> No ratings available")
        else:
            average = sum(ratings) / len(ratings)
            print(f"Corrected, ratings = {ratings} -> Average = {average:.2f}")


print(f"===== {FestivalScreening.festival_name} =====")
display_records()

while True:
    choice = input("\nAdd a new screening? (Y/N): ").strip().upper()
    if choice != "Y":
        break
    screening = collect_screening()
    print(screening)
    save_screening(screening)
    print("Screening saved to", RECORDS_FILE)

display_records()
file_pointer_demo()
debug_demo()
