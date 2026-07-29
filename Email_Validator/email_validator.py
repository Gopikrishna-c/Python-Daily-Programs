
print("***** Email Validator *****")
email = input("Enter your email: ")
if (
    email.count("@") == 1
    and "@" in email
    and "." in email
    and email.index("@") > 0
    and email.index(".") > email.index("@")
    and " " not in email
    and not email.endswith(".")
):
    print("Valid Email")
else:
    print("Invalid Email")