
def check_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
print("***** Leap Year Checker *****")

year = int(input("Enter a Year: "))

if check_leap_year(year):
    print(year, "is a Leap Year.")
else:
    print(year, "is Not a Leap Year.")