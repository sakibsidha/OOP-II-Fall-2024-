# 1
class InvalidVoterException(Exception):
    def __init__(self, message="Age is less than 18. Invalid voter."):
        super().__init__(message)

def check_voter_age(age):
    if age < 18:
        raise InvalidVoterException()
    else:
        print("You are eligible to vote.")

try:
    age = int(input("Enter your age: "))
    check_voter_age(age)
except InvalidVoterException as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a numeric value.")
except:
    print("Other Errors Occured.")
finally:
    print("Done.")


# 2
class SalaryNotInRange(Exception):
    def __init__(self, message="Salary is not in the range 10000 to 50000."):
        super().__init__(message)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_salary(self):
        if self.salary < 10000 or self.salary > 50000:
            raise SalaryNotInRange()
        else:
            print(f"Employee Name: {self.name}, Salary: {self.salary}")

try:
    name = input("Enter employee name: ")
    salary = int(input("Enter salary: "))
    emp = Employee(name, salary)
    emp.display_salary()
except SalaryNotInRange as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a numeric value.")
except:
    print("Other Errors Occured.")
finally:
    print("Done.")


# 3
arr = [10, 5, 15, 20]

try:
    divisor = int(input("Enter a divisor: "))
    for i in arr:
        print(f"Result: {i} / {divisor} = {i / divisor}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Division performed successfully.")
finally:
    print("Done.")


# 4
class InsufficientBalanceException(Exception):
    def __init__(self, message="Insufficient balance to withdraw the amount."):
        super().__init__(message)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceException()
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.balance}")

try:
    balance = float(input("Enter initial balance: "))
    account = BankAccount(balance)
    withdraw_amount = float(input("Enter amount to withdraw: "))
    account.withdraw(withdraw_amount)
except InsufficientBalanceException as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a numeric value.")
except:
    print("Other Errors Occured.")
finally:
    print("Done.")
