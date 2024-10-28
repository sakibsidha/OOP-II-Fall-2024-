class Person:
    def __init__(self, fname, lname):
        print("Person constructor")
        self.fname = fname
        self.lname = lname

    def display(self):
        print("First name:", self.fname)
        print("Last name:", self.lname)

class Student(Person):
    def __init__(self, fname, lname, graduation_year):
        print("Student constructor")
        super().__init__(fname, lname)
        self.graduation_year = graduation_year

    def display(self):
        super().display()
        print("Graduation Year:", self.graduation_year)

class Teacher(Person):
    def __init__(self, fname, lname, joining_year):
        print("Teacher constructor")
        Person.__init__(self, fname, lname)
        self.joining_year = joining_year

    def displayTeacher(self):
        super().display()
        print("Joining Year:", self.joining_year)

class Admin(Person):
    def __init__(self, fname, lname, joining_year):
        print("Admin constructor")
        Person.__init__(self, fname, lname)
        self.joining_year = joining_year

    def displayAdmin(self):
        super().display()
        print("Joining Year:", self.joining_year)

class CurrentStudent(Student):
    def __init__(self, fname, lname):
        print("CurrentStudent constructor")
        super().__init__(fname, lname, 2026)
        self.currentSemester = 5
    
    def display(self):
        super().display()
        print("Current Semester:", self.currentSemester)

class Alumni(Student):
    def __init__(self, fname, lname):
        print("Alumni constructor")
        super().__init__(fname, lname, 6746)
        self.passingYear = 1999
    
    def display(self):
        super().display()
        print("Passing Year:", self.passingYear)
        
class Employee(Teacher, Admin):
    def __init__(self, fname, lname, jyear, age):
        print("Employee constructor")
        Teacher.__init__(self, fname, lname, jyear)
        Admin.__init__(self, fname, lname, jyear)
        self.age = age

    def display(self):
        super().displayAdmin()
        super().displayTeacher()
        print(self.age)

student = Student("Tanjiro", "Kamado", 2026)
student.display()
person = Person("Nezuko", "Chan")
person.display()
teacher = Teacher("Raisa", "Hauqqqqqqe", 2026)
teacher.displayTeacher()
admin = Admin("Akhter", "Ali", 2022)
admin.displayAdmin()
current_student = CurrentStudent("Rakibul", "Islam")
current_student.display()
alumni = Alumni("Sajib", "Hossain")
alumni.display()
employee = Employee("Akij", "Bhai", 6766, 45)
employee.display()
