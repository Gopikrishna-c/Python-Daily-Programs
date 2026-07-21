
print("***********************Employee Salary Management System*******************************")
employee_name = input("Enter the Name: ")
employee_id = input("Enter the Employee id: ")
basic_salary = float(input("Enter the Employee salary: "))
HRA = basic_salary * 20 / 100
DA = basic_salary * 10 / 100
PF = basic_salary *12 / 100
net_salary = basic_salary+ HRA + DA - PF
print("Employee Name :", employee_name)
print("Employee Id :", employee_id)
print("Basic Salary :", basic_salary)
print("HRA:", HRA)
print("DA:", DA)
print("PF:", PF)
print("Net Salary:", net_salary)


