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

ob = Student("Tanjiro", "Kamado", 2026)
ob.display()
ob2 = Person("Nezuko", "Chan")
ob2.display()
