

print("***** Expense Tracker *****")
expenses = []
num = int(input("Enter the number of expenses: "))
for i in range(num):
    amount = float(input(f"Enter expense {i+1}: ₹"))
    expenses.append(amount)
print("\n----- Expense List -----")
for i in range(len(expenses)):
    print(f"Expense {i+1}: ₹{expenses[i]}")
print("\nTotal Expense: ₹", sum(expenses))