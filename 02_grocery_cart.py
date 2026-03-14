Groceries_menu = {
    "Sugar": 20,
    "Honey": 30,
    "Milk": 25,
    "Bread": 15,
    "Eggs": 40,
    "Rice": 50,
    "Butter": 35,
    "Cheese": 45,
    "Apple": 10,
    "Banana": 12
}

cart = {}  # {"Sugar":6, "milk": 4}  --> cart[0]= 6

while True:

    print("\n------------------- GROCERIES MENU -------------------")

    for item_name, price in Groceries_menu.items():  # Sugar ------ $20.00
        print(f"{item_name:<6}----------${price:.2f}")

    print("------------------------------------------------------")

    user_item = input(
        "Please enter grocery name (or type 'checkout'): ").title()
    # Checkout condition
    if user_item.lower() == "checkout":
        break

    # Search for item in groceries menu  :///https://www.tutorialspoint.com/python/python_exceptions.htm
    if user_item in Groceries_menu:
        try:
            quantity = int(input("Please enter quantity: "))
            if quantity <= 0:
                print(
                    f"{"\033[31m"} Quantity must be a positive number.{"\033[0m"}")
                continue

            # Add to cart or update quantity if already exists
            if user_item in cart:
                # previous qua=previous qua + quantity
                cart[user_item] += quantity
            else:
                cart[user_item] = quantity  # "milk":4
            print(f"{quantity} {user_item} added to cart.")
        except ValueError:
            print(
                f"{"\033[31m"}Invalid input.{"\033[0m"}")
    else:
        print("This grocery is not found in menu. Please enter an item from the menu. ")

    # Final bill display
if cart:
    print("\n_______________RECEIPT ________________\n")
    total = 0
    for grocery, quantity in cart.items():
        subtotal = Groceries_menu[grocery]*quantity
        print(f"{grocery} x {quantity:<8} ...........${subtotal:.2f}")
        total += subtotal  # total= total+subtotal
    print("_______________________________________")
    print(f"Total-----------------------${total:.2f}")
    print("\nThank you for shopping in our store.")

else:
    print("\nThank you for visiting our store!")
