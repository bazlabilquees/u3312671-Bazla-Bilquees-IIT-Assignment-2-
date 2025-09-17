# Name: Bazla Bilquees
# Student ID: u3312671
# Case Study: Campus Café Checkout with Meal Deal

# Prices menu: item -> (price, category)
menu = {
    "Coffee": (3.50, "Drink"),
    "Tea": (2.50, "Drink"),
    "Muffin": (2.00, "Food"),
    "Sandwich": (5.00, "Food"),
    "Smoothie": (4.00, "Drink"),
    "Salad": (4.50, "Food")
}

cart = []

# Function to display the menu
def show_menu():
    print("\n--- Café Menu ---")
    for item, (price, category) in menu.items():
        print(f"{item:10} - ${price:.2f} ({category})")
    print("----------------")

# Add item to cart
def add_item(cart):
    show_menu()
    item = input("Enter item to add: ").title()
    if item in menu:
        qty = input("Quantity (default 1): ").strip()
        qty = int(qty) if qty.isdigit() and int(qty) > 0 else 1
        cart.append((item, qty))
        print(f"{qty} x {item} added to cart.")
    else:
        print("Item not on the menu.")

# View current cart
def view_cart(cart):
    if not cart:
        print("Cart is empty.")
        return
    print("\n--- Current Cart ---")
    for item, qty in cart:
        price = menu[item][0]
        print(f"{qty} x {item} - ${price*qty:.2f}")
    print("--------------------")

# Checkout and print receipt
def checkout(cart):
    if not cart:
        print("Cart is empty. Nothing to checkout.")
        return

    subtotal = sum(menu[item][0]*qty for item, qty in cart)
    tax = subtotal * 0.10
    discount = 0.0

    # Student discount
    student = input("Apply student discount (5%)? (y/n): ").lower()
    if student == "y":
        discount = (subtotal + tax) * 0.05

    # Meal deal discount: $2 off per drink+food combo
    drinks = sum(qty for item, qty in cart if menu[item][1] == "Drink")
    foods = sum(qty for item, qty in cart if menu[item][1] == "Food")
    meal_deal_discount = 0
    combos = min(drinks, foods)
    if combos >= 1:
        meal_deal_discount = combos * 2.00

    total = subtotal + tax - discount - meal_deal_discount

    # Print receipt
    print("\n--- Receipt ---")
    for item, qty in cart:
        price = menu[item][0]
        print(f"{qty} x {item} - ${price*qty:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (10%): ${tax:.2f}")
    if discount > 0:
        print(f"Student discount: -${discount:.2f}")
    if meal_deal_discount > 0:
        print(f"Meal deal discount: -${meal_deal_discount:.2f}")
    print(f"Total: ${total:.2f}")
    print("Thank you for visiting!")

# Main program loop
def main():
    while True:
        print("\n--- Café POS ---")
        print("1. Show Menu\n2. Add Item\n3. View Cart\n4. Checkout\n5. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            show_menu()
        elif choice == "2":
            add_item(cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            checkout(cart)
            cart.clear()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
