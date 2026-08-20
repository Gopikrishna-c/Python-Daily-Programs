
print("***** Movie Ticket Booking *****")
tickets = []
while True:
    print("\n1. Book Ticket")
    print("2. View Tickets")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        movie = input("Enter Movie Name: ")
        tickets.append(movie)
        print("Ticket Booked!")
    elif choice == 2:
        print("\nBooked Movies:")
        for movie in tickets:
            print(movie)
    elif choice == 3:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")


        