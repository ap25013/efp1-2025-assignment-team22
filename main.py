from models import Product, Store, User
from services import (
    register_user, login_user, search_products,
    show_reviews, rate_product, users, products, current_user
)

# --- Seed sample products for testing ---
def seed_products():
    p1 = Product("iPhone 15", "Electronics", "Apple smartphone")
    p1.stores.append(Store("Skroutz", "skroutz.gr", 999))
    p1.stores.append(Store("BestPrices", "bestprices.gr", 979))

    p2 = Product("Galaxy S24", "Electronics", "Samsung smartphone")
    p2.stores.append(Store("Samsung Store", "samsung.com", 899))

    p3 = Product("AirPods Pro", "Electronics", "Apple wireless earbuds")
    p3.stores.append(Store("Apple Store", "apple.com", 249))
    p3.stores.append(Store("Amazon", "amazon.com", 239))

    products.extend([p1, p2, p3])

# --- Main program loop ---
def main():
    seed_products()  # add sample products

    while True:
        print("\n--- Product Review App ---")
        print("1. Register")
        print("2. Login")
        print("3. Search product")
        print("4. Exit")
        
        choice = input("Choice: ").strip()
        
        if choice == "1":
            # Ask for all User attributes
            username = input("Username: ")
            password = input("Password: ")
            gender = input("Gender: ")
            country = input("Country: ")
            age_group = input("Age group: ")

            user = User(username, password, gender, country, age_group)
            users.append(user)
            print("User registered successfully!")

        elif choice == "2":
            login_user()

        elif choice == "3":
            results = search_products()
            if not results:
                print("No products found.")
                continue

            print("\nProducts found:")
            for i, product in enumerate(results, 1):
                print(f"{i}. {product.name}")

            try:
                product_index = int(input("Select product: ")) - 1
                if product_index not in range(len(results)):
                    print("Invalid selection.")
                    continue

                product = results[product_index]
                print(f"\nProduct name: {product.name}")
                print(f"Category: {product.category}")
                print(f"Description: {product.description}")
                print("\nStores:")
                for store in product.stores:
                    print(f"{store.name} | {store.website} | {store.price}€")

                show_reviews_choice = input("\nShow reviews? (y/n): ").lower()
                if show_reviews_choice == "y":
                    show_reviews(product)

                rate_choice = input("Rate this product? (y/n): ").lower()
                if rate_choice == "y":
                    rate_product(product)

            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
