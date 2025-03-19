# student_management.py

import uuid

class Student:
    """Represents a student with basic information and enrolled courses."""
    
    def __init__(self, name, age, student_id=None):
        self.student_id = student_id if student_id else str(uuid.uuid4())[:8]
        self.name = name
        self.age = age
        self.courses = {}  # {Course: grade}

    def enroll(self, course):
        """Enroll the student in a course."""
        if course.course_code not in self.courses:
            self.courses[course.course_code] = None  # No grade assigned yet
            course.add_student(self)
            print(f"✅ {self.name} enrolled in {course.course_name}")
        else:
            print(f"⚠️ {self.name} is already enrolled in {course.course_name}")

    def assign_grade(self, course, grade):
        """Assign a grade to the student for a specific course."""
        if course.course_code in self.courses:
            self.courses[course.course_code] = grade
            print(f"📊 {self.name} received grade {grade} in {course.course_name}")
        else:
            print(f"⚠️ {self.name} is not enrolled in {course.course_name}")

    def get_report_card(self):
        """Generate a report card for the student."""
        return ReportCard(self)

    def __str__(self):
        return f"🎓 {self.name} (ID: {self.student_id}, Age: {self.age})"


class Course:
    """Represents a course with enrolled students."""
    
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = {}  # {Student: grade}

    def add_student(self, student):
        """Add a student to the course."""
        self.students[student.student_id] = student

    def __str__(self):
        return f"📚 {self.course_name} (Code: {self.course_code})"


class ReportCard:
    """Generates a report card for a student."""
    
    def __init__(self, student):
        self.student = student
        self.grades = student.courses

    def display(self):
        """Print the student's report card."""
        print(f"\n📜 Report Card for {self.student.name} (ID: {self.student.student_id})")
        for course_code, grade in self.grades.items():
            status = f"Grade: {grade}" if grade is not None else "Not graded yet"
            print(f"🔹 {course_code}: {status}")
        print("-" * 30)


# 🎯 Demonstration
if __name__ == "__main__":
    # Create students
    alice = Student("Alice Johnson", 20)
    bob = Student("Bob Smith", 22)

    # Create courses
    math = Course("Mathematics", "MATH101")
    physics = Course("Physics", "PHY201")

    # Enroll students in courses
    alice.enroll(math)
    alice.enroll(physics)
    bob.enroll(math)

    # Assign grades
    alice.assign_grade(math, "A")
    alice.assign_grade(physics, "B")
    bob.assign_grade(math, "B+")

    # Generate report cards
    alice.get_report_card().display()
    bob.get_report_card().display()
