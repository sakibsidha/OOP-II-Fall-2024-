from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class InvalidAmountException(Exception):
    pass

class AccountHolder(BankAccount):
    def __init__(self, name, balance, acc_num):
        self._balance = balance
        self.name = name
        self.__acc_num = acc_num
    
    def deposit(self, amount):
        if (amount < 0):
            raise InvalidAmountException
        self._balance += amount
        print("Deposit successful! New balance:", self._balance)
    
    def withdraw(self, amount):
        if (amount < 0):
            raise InvalidAmountException
        if (amount > self._balance):
            raise ValueError
        self._balance -= amount
        print("Withdraw successful! New balance:", self._balance)

    def setBalance(self, balance):
        self._balance = balance

    def setName(self, name):
        self.name = name

    def setAccountNum(self, acc_num):
        self.__acc_num =  acc_num
    
    def getBalance(self):
        return self._balance

    def getName(self):
        return  self.name

    def getAccountNum(self):
        return self.__acc_num

objects = []
for i in range(0, 5):
    name = input()
    balance = float(input())
    acc_num = int(input())
    a = AccountHolder(name, balance, acc_num)
    objects.append(a)

print(objects[2].getName())
a = objects[0]

try:
    a.deposit(1)
    a.withdraw(103)
except ValueError:
    print("Value Error Occured!")
except InvalidAmountException:
    print("Invalid Amount Exception Occured.")
except:
    print("Other errors occured!")
finally:
    print("Done.")
