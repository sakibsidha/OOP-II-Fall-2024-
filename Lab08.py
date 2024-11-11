# w3 schools

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")

# task
values = [10, 20, 3, 30, 0]
divisor = int(input())
try:
    for i in values:
        result = i / divisor
        print(result)
except ZeroDivisionError:
    print("Zero Division Error Occured")
except TypeError:
    print("Type Error Occured!")
except ValueError:
    print("Value Error Occured!")
except ArithmeticError:
    print("Arithmetic Error Occured!")
except:
    print("Error Occured")
finally:
    print("Done working with", i)

exception handling in class

class InsufficientBalanceError(Exception):
    pass
    
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientBalanceError
        else:
            self.balance -= amount
            print("Transaction Successful! New amount:", self.balance)

obito = BankAccount(100)
try:
    amount = int(input("Enter amount: "))
    obito.withdraw(amount)
except InsufficientBalanceError:
    print("Unsuccessful transaction!")
except:
    print("Errors Occured")
finally:
    print("Done")
