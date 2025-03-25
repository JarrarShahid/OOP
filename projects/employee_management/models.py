from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))
    salary = Column(Float, nullable=False)
    department = relationship("Department", back_populates="employees")

class Database:
    def __init__(self, db_url="sqlite:///employees.db"):
        self.engine = create_engine(db_url, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()

class EmployeeManager:
    def __init__(self, db: Database):
        self.db = db

    def add_employee(self, name, department_name, salary):
        session = self.db.get_session()
        try:
            department = session.query(Department).filter_by(name=department_name).first()
            if not department:
                department = Department(name=department_name)
                session.add(department)
                session.commit()
            
            employee = Employee(name=name, department=department, salary=salary)
            session.add(employee)
            session.commit()
            print(f"Employee {name} added successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error adding employee: {e}")
        finally:
            session.close()

    def list_employees(self):
        session = self.db.get_session()
        try:
            employees = session.query(Employee).all()
            for emp in employees:
                print(f"{emp.id}: {emp.name} - {emp.department.name} - ${emp.salary}")
        except Exception as e:
            print(f"Error fetching employees: {e}")
        finally:
            session.close()

if __name__ == "__main__":
    db = Database()
    manager = EmployeeManager(db)
    manager.add_employee("John Doe", "Engineering", 70000)
    manager.list_employees()
