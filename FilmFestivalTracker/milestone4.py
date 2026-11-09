import festival_utils


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

    def occupancy_rate(self):
        return festival_utils.calculate_occupancy(self.tickets_sold, self.capacity)

    def average_rating(self):
        return festival_utils.average_rating(self.ratings)

    def ticket_revenue(self):
        return self.tickets_sold * self.ticket_price

    def __str__(self):
        return (f"[{self.screening_id}] {self.film_title} ({self.genre}) | "
                f"Occupancy: {self.occupancy_rate():.2f}% | "
                f"Avg Rating: {self.average_rating():.2f} | "
                f"Revenue: Rs.{self.ticket_revenue():.2f}")


def occupancy_metric(screening):
    return f"{screening.film_title}: Occupancy = {screening.occupancy_rate():.2f}%"


def rating_metric(screening):
    return f"{screening.film_title}: Average Rating = {screening.average_rating():.2f}"


screenings = [
    FestivalScreening("THE28", "The Last Signal", "Sci-Fi", 120, 96, 150),
    FestivalScreening("SIL05", "Silent Valley", "Drama", 80, 52, 120),
    FestivalScreening("LAU10", "Laugh Track", "Comedy", 100, 100, 100),
    FestivalScreening("DAR15", "Dark Corridor", "Horror", 60, 25, 130),
]

all_ratings = [[5, 4, 5, 4], [3, 4, 3], [4, 5, 5], [2, 3, 2]]
for screening, ratings in zip(screenings, all_ratings):
    for r in ratings:
        screening.add_rating(r)

print("===== ALL SCREENINGS =====")
for screening in screenings:
    print(screening)

analytics = {"occupancy": occupancy_metric, "rating": rating_metric}

key = input("\nChoose analytics (occupancy/rating): ").strip().lower()
if key in analytics:
    print(f"\n===== {key.upper()} ANALYTICS =====")
    for screening in screenings:
        print(analytics[key](screening))
else:
    print("Invalid analytics key.")

ranked = sorted(screenings, key=lambda s: s.average_rating(), reverse=True)
print("\n===== RANKING BY AVERAGE RATING =====")
for position, screening in enumerate(ranked, start=1):
    print(f"{position}. {screening.film_title} - {screening.average_rating():.2f}")

print("\n===== DEFAULT / KEYWORD PARAMETERS =====")
print("Default discount (10%) on Rs.150:", festival_utils.discounted_price(150))
print("Keyword discount (25%) on Rs.150:", festival_utils.discounted_price(price=150, discount=0.25))
print("Keyword args, any order (20%) on Rs.120:", festival_utils.discounted_price(discount=0.20, price=120))
