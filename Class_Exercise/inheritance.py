# Base class: Person
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def display(self):
        print(f"Name: {self.firstName} {self.lastName}")

# Derived class: Student
class Student(Person):
    def __init__(self, firstName, lastName, graduationYear):
        super().__init__(firstName, lastName)
        self.graduationYear = graduationYear

    def display(self):
        super().display()
        print(f"Graduation Year: {self.graduationYear}")

# Derived class: Alumni (inherits Student)
class Alumni(Student):
    def __init__(self, firstName, lastName, graduationYear, passingYear):
        super().__init__(firstName, lastName, graduationYear)
        self.passingYear = passingYear

    def display(self):
        super().display()
        print(f"Passing Year: {self.passingYear}")

# Derived class: CurrentStudent (inherits Student)
class CurrentStudent(Student):
    def __init__(self, firstName, lastName, graduationYear, currentSemester):
        super().__init__(firstName, lastName, graduationYear)
        self.currentSemester = currentSemester

    def display(self):
        super().display()
        print(f"Current Semester: {self.currentSemester}")

# Derived class: Teacher
class Teacher(Person):
    def __init__(self, firstName, lastName, joiningYear):
        super().__init__(firstName, lastName)
        self.joiningYear = joiningYear

    def display(self):
        super().display()
        print(f"Joining Year: {self.joiningYear}")

# Derived class: Admin
class Admin(Person):
    def __init__(self, firstName, lastName, joiningYear):
        super().__init__(firstName, lastName)
        self.joiningYear = joiningYear

    def display(self):
        super().display()
        print(f"Joining Year: {self.joiningYear}")

# Derived class: Employee
class Employee(Person):
    def __init__(self, firstName, lastName, employeeId):
        super().__init__(firstName, lastName)
        self.employeeId = employeeId

    def display(self):
        super().display()
        print(f"Employee ID: {self.employeeId}")

print("\nTesting Student:")
s = Student("Sadman", "Sakib", 2024)
s.display()

print("\nTesting Alumni:")
a = Alumni("Abir", "Ahmed", 2020, 2021)
a.display()

print("\nTesting CurrentStudent:")
cs = CurrentStudent("Rawnok", "Haque", 2025, "Semester 4")
cs.display()

print("\nTesting Teacher:")
t = Teacher("Ms. Nasima", "Bithi", 2015)
t.display()

print("\nTesting Admin:")
ad = Admin("Abu", "Saleh", 2018)
ad.display()

print("\nTesting Employee:")
e = Employee("Negar", "Sultana", "E12345")
e.display()
