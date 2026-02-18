from models import User, Review

# In-memory storage
users = []
products = []
current_user = None


def register_user():
    # Register a new user
    username = input("Username: ")
    password = input("Password: ")
    gender =input ("Gender:")
    country = input("Country:")
    age_group =input("Age_group:")

    user = User(username, password,gender ,country ,age_group)
    users.append(user)

    print("User registered successfully!")
    return user


def login_user():
    # Login an existing user
    global current_user

    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user.username == username and user.password == password:
            current_user = user
            print("Login successful!")
            return user

    print("Wrong credentials.")
    return None


def search_products():
    # Search products by name or category
    keyword = input("Enter product name or category: ")
    results = []

    for product in products:
        if keyword.lower() in product.name.lower() or keyword.lower() in product.category.lower():
            results.append(product)

    return results


def show_product_details(product):
    # Display product information
    print("\nName:", product.name)
    print("Category:", product.category)
    print("Description:", product.description)

    print("\nStores:")
    for store in product.stores:
        print(f"{store.name} | {store.website} | {store.price}€")


def show_reviews(product):
    # Display all reviews of a product
    if not product.reviews:
        print("No reviews yet.")
        return

    for review in product.reviews:
        print(f"{review.date} | {review.user.username} | {review.rating} stars | {review.comment}")


def rate_product(product):
    # Allow current user to rate a product
    global current_user

    if current_user is None:
        print("You must login first.")
        return

    # Check if user already reviewed this product
    for review in product.reviews:
        if review.user == current_user:
            print("You have already reviewed this product.")
            return

    rating = int(input("Rating (1-5): "))
    comment = input("Comment: ")

    review = Review(current_user, product , rating, comment)

    product.reviews.append(review)
    current_user.reviews.append(review)

    print("Review submitted successfully!")
