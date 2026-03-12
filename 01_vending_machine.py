"""1)	Build a program that:
•	Displays a list of snacks and drinks with item numbers and prices. 
•	Ask the user to choose items by number in a loop.
•	 Keeps track of selected items and their prices.
•	Ends when the user types "done".
•	Finally prints a receipt showing: List of selected items with prices and total cost"""

snack_menu = {
    1: ("Greek yogurt with honey & berries", 20),
    2: ("Apple slices with peanut butter", 30.2),
    3: ("Mixed nuts (almonds, walnuts, cashews)", 40),
    4: ("Carrot & cucumber sticks with hummus", 70),
    5: ("Boiled eggs", 40),
    6: ("Avocado on whole-grain toast", 30),
    7: ("Cottage cheese with pineapple", 25.6),
    8: ("Smoothie (banana + spinach + almond milk)", 55)
}

cart = []
total = 0

while True:
    print("\n-------------------------MENU---------------------------------")
    for key, value in snack_menu.items():
        print(f"{key}. {value[0]:<45}  ..... ${value[1]:.2f}")
    print("--------------------------------------------------------------")

    user_snack = input(
        f"Please enter 1-{len(snack_menu)} for your snack to choose or/done to quit:")

    if user_snack.lower() == "done":
        break
    if user_snack.isdigit():
        if int(user_snack) in snack_menu:
            selected_item = snack_menu[int(user_snack)]
            cart.append(selected_item)
            print(f"\n{selected_item[0]} added!")
            total += selected_item[1]
        else:
            print("Item not found.")
    else:
        print("Invalid input.")

print("\n_________________________Your Receipts________________________\n")

for item in cart:
    print(f'{item[0]:<42} .....${item[1]:.2f}')

print(f"\nYour total bill is ${total:.2f}")
print("_______________________________________________________________")
print("THANK YOU!")