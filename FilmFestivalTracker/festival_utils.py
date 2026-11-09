def calculate_occupancy(tickets_sold, capacity):
    return tickets_sold / capacity * 100


def average_rating(ratings):
    if not ratings:
        return 0
    return sum(ratings) / len(ratings)


def discounted_price(price, discount=0.10):
    return price - price * discount
