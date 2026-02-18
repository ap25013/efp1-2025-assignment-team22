from models import Product, Store
from services import (register_user, login_user,search_products, 
    show_product_details, show_reviews, rate_product, 
    users, products,current_user
)


def main():
    #main 
   
    while True:
        print("\n1.Register")
        print("2.Login")
        print("3.Search product")
        print("4.Exit")
        
        choice = input("Choice: ")   
        
        if choice == "1":
            register_user()
        
        elif choice == "2":
            login_user()
        
        
        elif choice == "3":
            results = search_products()
            
            if not results:
                print("No products found.")
                continue
            
                
                            
            for i, product in enumerate(results, 1):
                print(f"{i}. {product.name}")
                
            1
            try:
                product_index = int(input("Select product: ")) - 1
                
                if product_index in range(len(results)):
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
                else:
                    print("Invalid selection.")
                    
            except ValueError: 
                print("Invalid input.")
        
        
        elif choice == "4":
            print("Exit")
            break
        
        else:
            print("Invalid choice.")



if __name__== "__main__":
    main()
