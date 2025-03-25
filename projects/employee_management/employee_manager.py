# Employee Manager
class EmployeeManager:
    def __init__(self, db):
        self.db = db

    def add_department(self, name):
        self.db.execute("INSERT INTO departments (name) VALUES (?)", (name,))

    def add_employee(self, name, age, department_name):
        department = self.db.fetch("SELECT id FROM departments WHERE name = ?", (department_name,))
        if department:
            department_id = department[0][0]
            self.db.execute("INSERT INTO employees (name, age, department_id) VALUES (?, ?, ?)", (name, age, department_id))
        else:
            print("Department not found!")

    def set_salary(self, employee_name, amount):
        employee = self.db.fetch("SELECT id FROM employees WHERE name = ?", (employee_name,))
        if employee:
            employee_id = employee[0][0]
            self.db.execute("INSERT INTO salaries (employee_id, amount) VALUES (?, ?)", (employee_id, amount))
        else:
            print("Employee not found!")

    def list_employees(self):
        employees = self.db.fetch("SELECT e.name, e.age, d.name FROM employees e JOIN departments d ON e.department_id = d.id")
        for emp in employees:
            print(f"Name: {emp[0]}, Age: {emp[1]}, Department: {emp[2]}")