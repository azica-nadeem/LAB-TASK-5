employees = []

for i in range(3):
    print("Enter information for employee", i +1)

    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    salary = int(input("Enter employee salary: "))

    employee = (name, age, salary)
    employees.append(employee)


print("\nEmployee Information")

for employee in employees:
    print(employee)