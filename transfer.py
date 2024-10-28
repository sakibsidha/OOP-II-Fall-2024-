class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print("First name:", self.fname)
        print("Last name:", self.lname)

class Student(Person):
    def __init__(self, fname, lname, graduation_year):
        super().__init__(fname, lname)
        self.graduation_year = graduation_year

    def display(self):
        super().display()
        print("Graduation Year:", self.graduation_year)

class Teacher(Person):
    def __init__(self, fname, lname, joining_year):
        super().__init__(fname, lname)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print("Joining Year:", self.joining_year)

class Admin(Person):
    def __init__(self, fname, lname, joining_year):
        super().__init__(fname, lname)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print("Joining Year:", self.joining_year)

class CurrentStudent(Student):
    def __init__(self, fname, lname):
        super().__init__(fname, lname, 2026)
        self.currentSemester = 5
    
    def display(self):
        super().display()
        print("Current Semester:", self.currentSemester)

class Alumni(Student):
    def __init__(self, fname, lname):
        super().__init__(fname, lname, 6746)
        self.passingYear = 1999
    
    def display(self):
        super().display()
        print("Passing Year:", self.passingYear)

ob = Student("Tanjiro", "Kamado", 2026)
ob.display()
ob2 = Person("Nezuko", "Chan")
ob2.display()
