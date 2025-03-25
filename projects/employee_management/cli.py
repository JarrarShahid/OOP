# CLI
if __name__ == "__main__":
    db = Database()
    manager = EmployeeManager(db)
    
    print("Employee Management System")
    while True:
        print("\n1. Add Department\n2. Add Employee\n3. Set Salary\n4. List Employees\n5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Enter department name: ")
            manager.add_department(name)
        elif choice == "2":
            name = input("Enter employee name: ")
            age = int(input("Enter age: "))
            dept = input("Enter department name: ")
            manager.add_employee(name, age, dept)
        elif choice == "3":
            name = input("Enter employee name: ")
            salary = float(input("Enter salary: "))
            manager.set_salary(name, salary)
        elif choice == "4":
            manager.list_employees()
        elif choice == "5":
            db.close()
            break
        else:
            print("Invalid choice!")