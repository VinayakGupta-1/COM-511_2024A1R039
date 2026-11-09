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
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            return True
        print(f"Invalid rating {rating} for {self.film_title}: must be 1-5.")
        return False

    def occupancy_rate(self):
        return self.tickets_sold / self.capacity * 100

    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def ticket_revenue(self):
        return self.tickets_sold * self.ticket_price

    def __str__(self):
        return (f"[{self.screening_id}] {self.film_title} ({self.genre}) | "
                f"Occupancy: {self.occupancy_rate():.2f}% | "
                f"Avg Rating: {self.average_rating():.2f} | "
                f"Revenue: Rs.{self.ticket_revenue():.2f}")


s1 = FestivalScreening("THE28", "The Last Signal", "Sci-Fi", 120, 96, 150)
s2 = FestivalScreening("SIL05", "Silent Valley", "Drama", 80, 52, 120)

for r in [5, 4, 5, 4]:
    s1.add_rating(r)
for r in [3, 4, 6, 3]:
    s2.add_rating(r)

print("Festival:", FestivalScreening.festival_name)
print(s1)
print(s2)
print("isinstance(s1, FestivalScreening):", isinstance(s1, FestivalScreening))
