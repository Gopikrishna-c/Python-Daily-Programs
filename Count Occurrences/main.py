print("*****Count Occurrences*****")
numbers = [10, 20, 10, 30, 20, 10, 40]
print("List:", numbers)
target = int(input("Enter the number: "))
count = 0
for i in range(len(numbers)):
    if numbers[i] == target:
        count += 1
print("Occurrences:", count)