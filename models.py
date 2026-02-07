from datetime import date


class User:
    # Represents a system user
    def __init__(self, username, password, gender, country, age_group):
        self.username = username
        self.password = password
        self.gender = gender
        self.country = country
        self.age_group = age_group
        self.reviews = []  # List of Review objects


class Store:
    # Represents an online store
    def __init__(self, name, website, price):
        self.name = name
        self.website = website
        self.price = price


class Review:
    # Represents a product review
    def __init__(self, user, product, rating, comment):
        self.user = user
        self.product = product
        self.rating = rating
        self.comment = comment
        self.date = date.today()


class Product:
    # Represents a product
    def __init__(self, name, category, description):
        self.name = name
        self.category = category
        self.description = description
        self.stores = []
        self.reviews = []

    def average_rating(self):
        # Calculate average rating
        if len(self.reviews) == 0:
            return 0
        return sum(r.rating for r in self.reviews) / len(self.reviews)

    def min_price(self):
        # Return minimum price from stores
        if len(self.stores) == 0:
            return 0
        return min(s.price for s in self.stores)


class Comparison:
    # Represents comparison between up to 3 products
    def __init__(self, products):
        self.products = products

    def show_comparison(self):
        for p in self.products:
            print("\nProduct:", p.name)
            print("Description:", p.description)
            print("Number of reviews:", len(p.reviews))
            print("Average rating:", p.average_rating())
            print("Number of stores:", len(p.stores))
            print("Minimum price:", p.min_price())
