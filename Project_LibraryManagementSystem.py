"""

Final Lab Project for OOP II

Library Management Sytem (v.01)

By, 
    Kh Sadman Sakib (63_M2, 0242220005101951)
    Ramesha Rawnok Haque (63_M2, 0242220005101665)

Submitted to,
    Nasima Islam Bithi
    Lecturer
    Daffodil International University

"""

from datetime import datetime, timedelta
from abc import ABC, abstractclassmethod

# Custom exceptions
class LibraryException(Exception):
    pass

class BookNotAvailableException(LibraryException):
    pass

# Base class using abstraction
class Person(ABC):
    def __init__(self, name, email, phone_number):
        self._name = name
        self._email = email
        self._phone_number = phone_number
    
    @abstractclassmethod
    def display_info(self):
        pass


# Staff class
class Staff(Person):
    def __init__(self, staff_id, name, email, phone_number, role):
        super().__init__(name, email, phone_number)
        self.staff_id = staff_id
        self.role = role

    def display_info(self):
        print(f" ID: {self.staff_id}, Name: {self._name}, Phone: {self._phone_number}, Role: {self.role}")

class Librarian(Staff):
    def __init__(self, librarian_id, name, email, phone_number):
        super().__init__(librarian_id, name, email, phone_number, role="Librarian")

    def manage_books(self):
        print(f"{self.name} is managing books.")

    def assist_members(self):
        print(f"{self.name} is assisting members.")

    def generate_reports(self):
        print(f"{self.name} generated reports.")

# Category class
class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

# Book class
class Book:
    def __init__(self, book_id, title, author, category, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.quantity = quantity

    def display_info(self):
        print(f"ID: {self.book_id}, Name: {self.title}, Author : {self.author}, Category : {self.category}, Quantity : {self.quantity}")

# Member class
class Member(Person):
    def __init__(self, member_id, name, address, phone_number, email, membership_type, registration_date):
        super().__init__(name, email, phone_number)
        self.member_id = member_id
        self.address = address
        self.membership_type = membership_type
        self.registration_date = registration_date

    def get_name(self):
        return self._name
    
    def display_info(self):
        return f" ID: {self.member_id}, Name: {self._name}, Membership: {self.membership_type}, Registration Date: {self.registration_date}"


# Transaction class
class Transaction:
    def __init__(self, transaction_id, issue_date, due_date, return_date=None, fine_amount=0.0):
        self.transaction_id = transaction_id
        self.issue_date = issue_date
        self.due_date = due_date
        self.return_date = return_date
        self.fine_amount = fine_amount

    def issue_book(self, book, member):
        if book.quantity <= 0:
            raise BookNotAvailableException(f"Book {book.title} is not available.")
        book.quantity -= 1

    def return_book(self, book, member):
        self.return_date = datetime.now()
        if self.return_date > self.due_date:
            self.calculate_fine()
        book.quantity += 1

    def calculate_fine(self):
        days_late = (self.return_date - self.due_date).days
        if days_late > 0:
            self.fine_amount = days_late * 5  # Assume $5 per day
            print(f"Fine for late return: ${self.fine_amount}")

# Adding staffs (dictionary)
staffs = {
    1: Staff(1, "Rakibul Islam", "rakibulislam@gmail.com", "01872643102", "Janitor"),
    2: Staff(2, "Joy Hasan", "joyhasan@gmail.com", "01389758493", "Library Assistant"),
    3: Staff(4, "Lucky Akhand", "luckyakhand@gmail.com", "01945827485", "IT Specialist"),
}

# Adding librarians (dictionary)
librarians = {
    1: Librarian(1, "Azad Hossain", "azadhossain@gmail.com", "01782979277")
}

# Adding categories (tuple)
categories = (
    Category(1, "Fiction"),
    Category(2, "Science"),
    Category(3, "History"),
    Category(4, "Technology"),
)

# Adding members (list)
members = []
members.append(Member(1, "Abul Hossain", "45/B Dhanmondi, Dhaka", "01784567890", "abul.hossain@gmail.com", "Regular", datetime.now()))
members.append(Member(2, "Karim Ahmed", "12/A Banani, Dhaka", "01894567123", "karim.ahmed@gmail.com", "Premium", datetime.now()))

# Adding books (list)
books = []
books.append(Book(1, "The Alchemist", "Paulo Coelho", "Fiction", 5))
books.append(Book(2, "Sapiens", "Yuval Noah Harari", "History", 2))
books.append(Book(3, "The Art of Computer Programming", "Donald Knuth", "Technology", 3))
books.append(Book(4, "A Brief History of Time", "Stephen Hawking", "Science", 4))

transactions = []

def find_books_by_category(category_name):
    books_in_category = filter(lambda book: book.category.lower() == category_name.lower(), books)
    return list(books_in_category)

users = {
    "sakibsidha" : "sakib2003",
    "rawnok-haque" : "1234"
}

users_member = {
    "sakibsidha" : "sakib2003"
}

users_admin = {
    "rawnok-haque" : "1234"
}

issued_books = [] # [id, member_id, book_id]

def IssueBook():
    print("\n<< Issue Book >>\n")
    try:
        book_id = int(input("Enter Book ID to issue: "))
        member_id = int(input("Enter Member ID: "))
        book_to_issue = next((b for b in books if b.book_id == book_id), None)
        member = next((m for m in members if m.member_id == member_id), None)
        if not book_to_issue:
            print(f"No book found with ID {book_id}.\n")
            return 0
        if not member:
            print(f"No member found with ID {member_id}.\n")
            return 0
        due_date = datetime.now() + timedelta(days=14)
        transaction = Transaction(len(transactions) + 1, datetime.now(), due_date)
        transaction.issue_book(book_to_issue, member)
        transactions.append(transaction)
        lst = []
        lst.append(len(transactions))
        lst.append(member_id)
        lst.append(book_id)
        issued_books.append(lst)
        print(f"Book '{book_to_issue.title}' issued to {member.get_name()}. Due Date: {due_date.strftime('%Y-%m-%d')}\n")

    except BookNotAvailableException as e:
        print(f"Error: {e}\n")
    except Exception as e:
        print(f"Error occurred: {e}\n")

def ReturnBook():
    try:
        book_id = int(input("Enter Book ID to return: "))
        member_id = int(input("Enter Member ID: "))
        book_to_return = next((b for b in books if b.book_id == book_id), None)
        member = next((m for m in members if m.member_id == member_id), None)
        if not book_to_return:
            print(f"No book found with ID {book_id}.\n")
            return 0
        if not member:
            print(f"No member found with ID {member_id}.\n")
            return 0
        idx = -1
        for i in range (0, len(issued_books)):
            if issued_books[i][1] == member_id and issued_books[i][2] == book_id:
                idx = i
                break
        if idx == -1:
            print("\nNo book issued to this member or the book ID is not correct. Try again.")
            return 0
        transaction = Transaction(len(transactions) + 1, datetime.now(), datetime.now())
        transaction.return_book(book_to_return, member)
        transactions.append(transaction)
        print(f"Book '{book_to_return.title}' returned by {member.get_name()}.\n")
        del issued_books[idx]
    except Exception as e:
        print(f"Error occurred: {e}\n")

demanded_books = []

def DemandNewBooks():
    name = input("Book name: ")
    author = input("Author's name: ")
    lst = []
    lst.append(name)
    lst.append(author)
    demanded_books.append(lst)
    print(f"\nAn admin will review your request soon!\n")

def UserInterface():
    print("\n<< User Interface >>\n")
    print("Choose what you want to do:\n 1. View Books\n 2. Demand New Books\n 3. Log Out\n")
    try:
        inp = int(input())
    except Exception as e:
        print(f"\nError occurred: {e}\nTry again.\n")
        return UserInterface()
    if inp == 1:
        ViewBooks()
        return UserInterface()
    elif inp == 2:
        DemandNewBooks()
        return UserInterface()
    elif inp == 3:
        return 0
    else:
        print("\nInvalid input. Try again.")
        return UserInterface()

def AddNewBook():
    try:
        book_id = books[-1].book_id + 1 if books else 1
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        category = input("Enter Book Category: ")
        quantity = int(input("Enter Book Quantity: "))
        new_book = Book(book_id, title, author, category, quantity)
        books.append(new_book)
        print(f"\nBook '{title}' added successfully.\n")
    except Exception as e:
        print(f"Error occurred: {e}\nTry again.\n")

def ShowTransaction():
    if not transactions:
        print("No transactions available.\n")
    else:
        print("All transactions:")
        for transaction in transactions:
            print(f"Transaction ID: {transaction.transaction_id}, Issue Date: {transaction.issue_date}, Due Date: {transaction.due_date}, Return Date: {transaction.return_date}, Fine: ${transaction.fine_amount:.2f}")
    print("")
    
def ShowDemanded():
    if not demanded_books:
        print("\nNo demanded books yet.\n")
    else:
        print("Demanded books:")
        for i in range (0, len(demanded_books)):
            print(f"Book Name: {demanded_books[i][0]}, Book Author: {demanded_books[i][1]}")
        print("")
        

def ManageBooks():
    print(f"\n<< Book Management >>\n\nChoose what you want to do:\n 1. View Books\n 2. Add New Book\n 3. Issue Book\n 4. Return Book\n 5. Show All Transactions\n 6. Show Demanded Books\n 7. Exit\n")
    try:
        inp = int(input())
    except Exception as e:
        print(f"\nError occurred: {e}\nTry again.\n")
        return ManageBooks()
    if inp == 1:
        ViewBooks()
        return ManageBooks()
    elif inp == 2:
        AddNewBook()
        return ManageBooks()
    elif inp == 3:
        IssueBook()
        return ManageBooks()
    elif inp == 4:
        ReturnBook()
        return ManageBooks()
    elif inp == 5:
        ShowTransaction()
        return ManageBooks()
    elif inp == 6:
        ShowDemanded()
        return ManageBooks()
    elif inp == 7:
        return 0
    else:
        print("\nInvalid input. Try again.")
        return ManageBooks()

def ManageMembers():
    print(f"\n << Member Management >> \n\nChoose what you want to do:\n 1. Show all members\n 2. Add member\n 3. Delete member\n 4. Exit\n")
    try:
        t = int(input())
    except Exception as e:
        print(f"\nError occurred: {e}\nTry again.\n")
        return ManageMembers()
    if t == 1:
        print("\nAll Members:")
        for member in members:
            print(member.display_info())
        print("")
        return ManageMembers()
    elif t == 2:
        print("\nAdd New Member:")
        try:
            member_id = members[len(members)-1].member_id + 1 
            name = input("Enter Member Name: ")
            address = input("Enter Member Address: ")
            phone_number = input("Enter Member Phone Number: ")
            email = input("Enter Member Email: ")
            membership_type = input("Enter Membership Type (Regular/Premium): ")
            registration_date = datetime.now()
            new_member = Member(member_id, name, address, phone_number, email, membership_type, registration_date)
            members.append(new_member)
            print(f"\nMember {name} added successfully.\n")
            return ManageMembers()
        except Exception as e:
            print(f"Error occurred: {e}\nTry again.\n")
            return ManageMembers()
    elif t == 3:
        print("\nDelete Member:")
        try:
            member_id = int(input("Enter Member ID to delete: "))
            member_to_delete = next((m for m in members if m.member_id == member_id), None)
            if member_to_delete:
                members.remove(member_to_delete)
                print(f"Member ID {member_id} deleted successfully.\n")
            else:
                print("Member not found.\n")
            return ManageMembers()
        except:
            print("Invalid Input. Try again.\n")
            return ManageMembers()
    elif t == 4:
        print("Exiting to Home...\n")
        return 0
    else:
        print("Invalid option. Try Again.\n")
        return ManageMembers()

def ManageLibrarian():
    while True:
        print(f"\n << Librarian Management >> \n\nChoose what you want to do:\n 1. See all librarians\n 2. Add librarian\n 3. Exit\n")
        try:
            t = int(input())
            print("")
        except:
            print("Invalid Input. Try again.\n")
            continue
        if t == 1:
            print("All Librarians:")
            for librarian in librarians.values():
                librarian.display_info()
            print("")
        elif t == 2:
            print("Add New Librarian:")
            try:
                librarian_id = len(librarians) + 1
                name = input("Enter Librarian Name: ")
                email = input("Enter Librarian Email: ")
                phone_number = input("Enter Librarian Phone Number: ")
                new_librarian = Librarian(librarian_id, name, email, phone_number)
                librarians[librarian_id] = new_librarian
                print(f"\nLibrarian {name} added successfully.\n")
            except Exception as e:
                print(f"Error occurred: {e}\nTry again.\n")
        elif t == 3:
            print("Exiting...\n")
            break
        else:
            print("Invalid option. Try again.\n")
            continue

def ManageStaffs():
    while True:
        print(f"\n<< Staff Management >> \n\nChoose what you want to do:\n 1. See all staffs\n 2. See all janitors\n 3. See all library assistants\n 4. See all IT specialists\n 5. Add staff\n 6. Exit\n")
        try:
            t = int(input())
            print("")
        except:
            print(" Invalid Input. Try again.\n")
            continue
        if t == 1:
            print("\nAll Staff Members:")
            for staff in staffs.values():
                staff.display_info()
            print("")
        elif t == 2:
            print("\nAll Janitors:")
            janitors = filter(lambda s: s.role.lower() == "janitor", staffs.values())
            for janitor in janitors:
                janitor.display_info()
            print("")
        elif t == 3:
            print("\nAll Library Assistants:")
            library_assistants = filter(lambda s: s.role.lower() == "library assistant", staffs.values())
            for assistant in library_assistants:
                assistant.display_info()
            print("")
        elif t == 4:
            print("\nAll IT Specialists:")
            it_specialists = filter(lambda s: s.role.lower() == "it specialist", staffs.values())
            for specialist in it_specialists:
                specialist.display_info()
            print("")
        elif t == 5:
            print("\nAdd New Staff Member:")
            try:
                staff_id = len(staffs) + 1
                name = input("Enter Staff Name: ")
                email = input("Enter Staff Email: ")
                phone_number = input("Enter Staff Phone Number: ")
                role = input("Enter Staff Role (Janitor, IT Specialist, Library Assistant): ")
                new_staff = Staff(staff_id, name, email, phone_number, role)
                staffs[staff_id] = new_staff
                print(f"\nStaff {name} added successfully.\n")
            except Exception as e:
                print(f"Error occurred: {e}\nTry again.\n")
        elif t == 6:
            print("Exiting to Home...\n")
            break
        else:
            print("Invalid option. Try again.\n")
            continue

def AdminInterface():
    print("\n<< Admin Interface >>\n\nChoose what you want to do:\n 1. Manage Books\n 2. Manage Members\n 3. Manage Librarians\n 4. Manage Staffs\n 5. Log Out\n")
    try:
        inp = int(input())
    except Exception as e:
        print(f"\nError occurred: {e}\nTry again.\n")
        return AdminInterface()
    if inp == 1:
        ManageBooks()
        return AdminInterface()
    elif inp == 2:
        ManageMembers()
        return AdminInterface()
    elif inp == 3:
        ManageLibrarian()
        return AdminInterface()
    elif inp == 4:
        ManageStaffs()
        return AdminInterface()
    elif inp == 5:
        return 0
    else:
        print("\nInvalid input. Try again.")
        return AdminInterface()
        

def SignIn():
    username = input("\nusername: ")
    password = input("password: ")
    fl = False
    for x, y in users.items():
        if x == username and y == password:
            fl = True
            break
    if fl == True:
        for x, y in users_member.items():
            if (x == username and y == password):
                UserInterface()
                return 0
        for x, y in users_admin.items():
            if (x == username and y == password):
                AdminInterface()
                return 0
        print("\nInternal Error Occured. Redirecting to Start Page")
        return 0
    else:
        print(f"\nCredentials not found.\n\n 1. Try Again\n 2. Sign Up\n 3. Exit\n")
        while True:
            try:
                inp = int(input())
            except Exception as e:
                print(f"Error occurred: {e}\nTry again.\n")
                continue
            if inp == 1:
                return SignIn()
            elif inp == 2:
                return SignUp()
            elif inp == 3:
                return 0
            else:
                print("\nInvalid input. Try again.")
                continue

def createUser(tt):
    username = input("\nEnter a username: ")
    pass1 = input("Enter password: ")
    pass2 = input("Re-enter password: ")
    if pass1 != pass2:
        print(f"\nThe two passwords don't match. Try again.\n")
        return SignUp()
    for x in users.keys():
        if x == username:
            print("\nUsername already exists.")
            return SignUp()
    users[username] = pass1
    if tt == 1:
        users_member[username] = pass1
    else:
        users_admin[username] = pass1
    print("\nAccount Created Successfully! You can now Sign In with the credentials.")
    return 1

def SignUp():
    print("\nSign-up as:\n 1. Library Member\n 2. Administration\n 3. Exit\n")
    try:
        inp  = int(input())
    except Exception as e:
        print(f"\nError occurred: {e}\nTry again.\n")
        return SignUp()
    if inp == 1:
        return createUser(1)
    elif inp == 2:
        secret_key = input("\nEnter the secret key (hint: OOPII): ") # OOPII
        if (secret_key == "OOPII"):
            return createUser(2)
        else:
            print("\nIncorrect key. Try again.")
            return SignUp()
    elif inp == 3:
        return 0
    else:
        print("Invalid input. Try again.")
        return SignUp()

def AboutUs():
    print("\n Library Management System (v.01)\n\n Developed by:\n  Kh Sadman Sakib (63_M2, ID: 1951)\n  Ramesha Rawnok Haque (63_M2, ID: 1665)\n\n Submitted to:\n  Nasima Islam Bithi\n  Lecturer\n  Daffodil International University\n")
    print(" Redirecting to Home...\n")

def ViewBooks():
    print(f"\n<< Book Management >>\n\nChoose what you want to do:\n 1. See all books\n 2. Find books by category\n 3. Exit\n")
    try:
        t = int(input())
    except Exception as e:
        print(f"Error occurred: {e}\nTry again.\n")
        return ViewBooks()
    if t == 1:
        print("\nAll Books:")
        for book in books:
            book.display_info()
        print("")
        return ViewBooks()

    elif t == 2:
        print("\nFind Books by Category:")
        try:
            category_name = input("Enter category name (Fiction, Science, History, Technology): ")
            books_in_category = find_books_by_category(category_name)
            if books_in_category:
                print(f"\nBooks in category '{category_name}':")
                for book in books_in_category:
                    book.display_info()
            else:
                print(f"\nNo books found in category '{category_name}'.\n")
            print("")
        except Exception as e:
            print(f"Error occurred: {e}\n")
        return ViewBooks()
    elif t == 3:
        return 0
    else:
        print("Invalid input. Try again.")
        return ViewBooks()
        
while True:
    print(f"\n$$ Welcome to Library Management System $$\n\nChoose what you want to do:\n 1. Sign In \n 2. Sign Up\n 3. About Us\n 4. Exit\n")
    try:
        inp  = int(input())
    except Exception as e:
        print(f"Error occurred: {e}\nTry again.\n")
        continue
    if inp == 1:
        SignIn()
    elif inp == 2:
        t = SignUp()
    elif inp == 3:
        AboutUs()
        continue
    elif inp == 4:
        print(f"Thanks for your time. Have a good day!")
        break
