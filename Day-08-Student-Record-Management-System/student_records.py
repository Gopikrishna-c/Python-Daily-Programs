def add_student():
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")
    with open("students.txt", "a") as file:
        file.write(f"Name: {name}, Age: {age}, Course: {course}\n")
    print("Student record added successfully!\n")
def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.read()
            if data:
                print("\n----- Student Records -----")
                print(data)
            else:
                print("No records found.")
    except FileNotFoundError:
        print("No student records found.")
while True:
    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")