password = input("Enter your password: ")

if len(password) < 6:
    print("Weak Password")
elif len(password) < 10:
    print("Medium Password")
else:
    print("Strong Password")