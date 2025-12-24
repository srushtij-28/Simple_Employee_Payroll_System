import os

FILE_NAME = "employees.txt"


# ---------- FILE FUNCTIONS ----------
def load_employees():
    employees = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                emp_id, name, salary = line.strip().split(",")
                employees[emp_id] = {
                    "name": name,
                    "salary": float(salary)
                }
    return employees


def save_employees(employees):
    with open(FILE_NAME, "w") as file:
        for emp_id, data in employees.items():
            file.write(f"{emp_id},{data['name']},{data['salary']}\n")


# ---------- MAIN PROGRAM ----------
employees = load_employees()

while True:
    print("\n====== EMPLOYEE PAYROLL SYSTEM ======")
    print("1. Add Employee")
    print("2. Generate Salary Slip")
    print("3. Update Salary")
    print("4. View All Employees")
    print("5. Exit")

    choice = input("Enter choice: ")

    # 1. ADD EMPLOYEE
    if choice == "1":
        emp_id = input("Employee ID: ")
        name = input("Employee Name: ")
        salary = float(input("Basic Salary: "))

        employees[emp_id] = {
            "name": name,
            "salary": salary
        }
        save_employees(employees)
        print("✅ Employee added successfully!")

    # 2. SALARY SLIP
    elif choice == "2":
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            salary = employees[emp_id]["salary"]

            hra = salary * 0.20
            da = salary * 0.10
            bonus = salary * 0.05
            pf = salary * 0.08
            tax = salary * 0.05

            gross = salary + hra + da + bonus
            net = gross - (pf + tax)

            print("\n------ SALARY SLIP ------")
            print("Employee ID :", emp_id)
            print("Name        :", employees[emp_id]["name"])
            print("Basic Salary:", salary)
            print("HRA         :", hra)
            print("DA          :", da)
            print("Bonus       :", bonus)
            print("PF          :", pf)
            print("Tax         :", tax)
            print("------------------------")
            print("Net Salary  :", net)

        else:
            print("❌ Employee not found")

    # 3. UPDATE SALARY
    elif choice == "3":
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            new_salary = float(input("Enter new salary: "))
            employees[emp_id]["salary"] = new_salary
            save_employees(employees)
            print("✅ Salary updated successfully!")
        else:
            print("❌ Employee not found")

    # 4. VIEW EMPLOYEES
    elif choice == "4":
        if not employees:
            print("No employees available")
        else:
            print("\n--- EMPLOYEE LIST ---")
            for emp_id, data in employees.items():
                print(emp_id, "-", data["name"], "-", data["salary"])

    # 5. EXIT
    elif choice == "5":
        print("👋 Exiting Payroll System. Thank you!")
        break

    else:
        print("⚠️ Invalid choice. Try again.")
