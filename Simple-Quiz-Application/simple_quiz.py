print("********** Simple Quiz Application **********")
score = 0
answer = input("1. What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct Answer")
    score += 1
else:
    print("Wrong")
answer = input("2. How many days are there in one month? ")
if answer == "30":
    print("Correct Answer")
    score += 1
else:
    print("Wrong")
answer = input("3. Which language is used to create Django framework? ")
if answer.lower() == "python":
    print("Correct Answer")
    score += 1
else:
    print("Wrong")

print("\nYour Final Score:", score, "/3")