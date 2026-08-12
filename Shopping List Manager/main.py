

print("***** Shopping List *****")

shopping_list = []

while True:
    print("\n1. Add Item")
    print("2. View List")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item: ")
        shopping_list.append(item)
        print("Item added!")

    elif choice == 2:
        print("\nShopping List:")
        for item in shopping_list:
            print(item)

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice")