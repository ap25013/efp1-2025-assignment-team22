from datetime import date

#attributes based the UML 
class RegisteredUser:
  def __init__(self, username, email, password, gender, country, age_group):
        self.username = username
        self.email = email
        self.password = password
        self.gender = gender
        self.country = country
        self.age_group = age_group
        self.reviews = []   

  def __str__(self): 
        return f"Hello: {self.username}"



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