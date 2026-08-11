


print("Armstrong Number Checker")
number = int(input("Enter the number :"))
original = number
total = 0

while number > 0:
    digit = number % 10
    total = total + digit ** 3
    number = number // 10

if total == original:
    print("Is an Armstrong Number")
else:
    print("Is not an Armstrong Number")





    