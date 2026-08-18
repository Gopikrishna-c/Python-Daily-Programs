


numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]
n = 10
expected_sum = n * (n + 1) // 2
actual_sum = 0
print("***** Missing Number Finder *****")
for num in numbers:
    actual_sum += num
missing_number = expected_sum - actual_sum
print("Numbers:", numbers)
print("Missing Number:", missing_number)