
# -------- MOVIE DATA --------
movies = {
    "Avatar": {"time": "6:00 PM", "price": 15},
    "Batman": {"time": "8:00 PM", "price": 12},
    "Harry Potter": {"time": "5:30 PM", "price": 10}
}

# -------- BOOKING STORAGE --------
total_cost = 0
total_tickets = 0


# -------- SHOW MOVIES --------
def show_movies():
    print("\n====== MOVIES AVAILABLE ======")

    movie_list = list(movies.items())

    for i, (name, info) in enumerate(movie_list, start=1):
        print(
            f"{i}. {name:<15} | Time: {info['time']} | Price: ${info['price']}")

    return movie_list


# -------- BOOK MOVIE --------
def book_movie():
    global total_cost, total_tickets

    movie_list = show_movies()

    try:
        choice = int(input("\nSelect movie number: "))

        if choice < 1 or choice > len(movie_list):
            print("Invalid movie number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    # Get movie information
    movie_name, movie_info = movie_list[choice - 1]

    try:
        qty = int(input("How many tickets? "))

        if qty <= 0:
            print("Ticket number must be positive.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    price = movie_info["price"]
    cost = qty * price

    print("\n------ BOOKING SUMMARY ------")
    print(f"Movie: {movie_name}")
    print(f"Showtime: {movie_info['time']}")
    print(f"Tickets: {qty}")
    print(f"Price per ticket: ${price}")
    print(f"Total cost: ${cost}")

    confirm = input("Confirm booking? (yes/no): ").lower()

    if confirm == "yes":
        total_cost += cost
        total_tickets += qty
        print("Booking confirmed!")
    else:
        print("Booking cancelled.")


# -------- MAIN PROGRAM --------
while True:

    book_movie()

    again = input("\nBook another movie? (yes/no): ").lower()

    if again == "no":
        break


# -------- FINAL SUMMARY --------
print("\n========= BOOKING SUMMARY =========")
print(f"Total tickets booked: {total_tickets}")
print(f"Total revenue: ${total_cost}")
print("Thank you for using the system!")
