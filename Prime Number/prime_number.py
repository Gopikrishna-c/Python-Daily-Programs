def check_prime(number):
    if number<2:
        return False
    for i in range(2,number):
        if number % i==0:
            return False
    return True

print("*****Prime Number Checker*****")
number =int(input("Enter a Number :"))
if check_prime(number):
    print(number, "Is a prime number")
else:
    print(number, "Is not a prime number")
