class Department:
    def __init__(self, name):
        self.name = name

    def displayName(self):
        print(f"Department: {self.name}")

class Teachers(Department):
    def scheduleClass(self):
        print("Class has been scheduled.")

    def gradeStudent(self):
        print("Student has been graded.")

    def displayName(self):
        print("Teacher's Department")

class Authors:
    def writeArticle(self):
        print("Article has been written.")

    def publishBlog(self):
        print("Blog has been published.")

    def displayName(self):
        print("Author's Profile")

class TeachersAuthor(Teachers, Authors):
    def profile(self):
        print("This is a Teacher-Author profile.")


ta = TeachersAuthor("Computer Science")

ta.displayName()
ta.scheduleClass() 
ta.gradeStudent()
ta.writeArticle()
ta.publishBlog()
ta.profile() 
