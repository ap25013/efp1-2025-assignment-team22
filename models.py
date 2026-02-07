from datetime import date

class User:
    # Represents a system user
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.reviews = []  # Reviews created by this user


class Store:
    # Represents an online store
    def __init__(self, name, website, price):
        self.name = name
        self.website = website
        self.price = price


class Review:
    # Represents a product review
    def __init__(self, user, rating, comment):
        self.user = user
        self.rating = rating
        self.comment = comment
        self.date = date.today()


class Product:
    # Represents a product
    def __init__(self, name, category, description):
        self.name = name
        self.category = category
        self.description = description
        self.stores = []   # List of Store objects
        self.reviews = []  # List of Review objects