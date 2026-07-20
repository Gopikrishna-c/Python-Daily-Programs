# Student Grade Calculator
marks = []
print("Enter marks for 5 subjects:")

for i in range(5):
    mark = float(input(f"Subject {i+1}: "))
    marks.append(mark)
# Calculate total and average
total = sum(marks)
average = total / len(marks)
# Find grade
if average >= 90:
    grade = "A+"
    message = "Excellent Performance!"
elif average >= 80:
    grade = "A"
    message = "Very Good!"
elif average >= 70:
    grade = "B"
    message = "Good Job!"
elif average >= 60:
    grade = "C"
    message = "Keep Improving!"
else:
    grade = "Fail"
    message = "Need More Practice!"
# Find highest and lowest marks
highest = max(marks)
lowest = min(marks)
# Display Result
print("\n------ Result ------")
print("Marks:", marks)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Grade:", grade)
print(message)