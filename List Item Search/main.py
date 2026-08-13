print("***** List Item Search *****")

items = ["apple", "banana", "orange", "mango"]

search = input("Enter an item: ").lower()

if search in items:
    print("Item found in the list!")
else:
    print("Item not found in the list!")