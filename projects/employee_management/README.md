# Employee Management System (Database-Backed)

## Overview  
This is an **object-oriented** Employee Management System built using **Python** and **SQLAlchemy**. It allows businesses to **add, manage, and view employees**, along with their **departments and salaries**, using a **database-backed** approach.

## Features  
✅ **Add Employees**: Register new employees with name, department, and salary.  
✅ **Manage Departments**: Automatically creates departments if they don’t exist.  
✅ **View Employees**: List all employees along with their department and salary.  
✅ **Persistent Storage**: Uses **SQLite** for storing employee and department data.  

## Installation  

1. **Clone the Repository**  
```sh
git clone https://github.com/JarrarShahid/OOP.git
cd OOP-Python-Showcase/projects/employee_management
```

2. **Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install Dependencies**
```sh
pip install -r requirements.txt
```

4. **Run the Application**
```sh
python main.py
```

## Usage

To add an employee, follow the CLI prompts after running python cli.py.

To list all employees, select the appropriate option from the menu.

## File Structure
```sh
employee_management/
│── main.py               # Entry point for the employee management system
│── models.py             # Defines Employee, Department, and Salary models
│── employee_manager.py   # Business logic for employee operations
│── cli.py                # Command-line interface for managing employees
│── storage.py            # Handles database operations using SQLAlchemy
│── requirements.txt      # List of dependencies
│── README.md             # Documentation for the project
```

## Dependencies
🚀 Python 3.8+

🚀 SQLAlchemy (For database interactions)

🚀 SQLite (Default database, can be changed to PostgreSQL)


