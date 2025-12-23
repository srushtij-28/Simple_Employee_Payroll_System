
employees = {}

while True:
    print("\n====== EMPLOYEE PAYROLL SYSTEM ======")
    print("1. Add Employee")
    print("2. Generate Salary Slip")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Employee ID: ")
        name = input("Employee Name: ")
        basic_salary = float(input("Basic Salary: "))

        employees[emp_id] = {
            "name": name,
            "salary": basic_salary
        }
        print("Employee added successfully!")

    elif choice == "2":
        if not employees:
            print("No employees found.")
            continue

        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            salary = employees[emp_id]["salary"]

            hra = salary * 0.20
            da = salary * 0.10
            tax = salary * 0.05

            gross_salary = salary + hra + da
            net_salary = gross_salary - tax

            print("\n------ SALARY SLIP ------")
            print("Employee ID:", emp_id)
            print("Name:", employees[emp_id]["name"])
            print("Basic Salary:", salary)
            print("HRA:", hra)
            print("DA:", da)
            print("Tax:", tax)
            print("Net Salary:", net_salary)

        else:
            print("Employee not found!")

    elif choice == "3":
        print("Thank you for using Payroll System!")
        break

    else:
        print("Invalid choice. Try again.")
