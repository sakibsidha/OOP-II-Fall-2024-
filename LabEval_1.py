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
        self.__name = name
        self.__acc_num = acc_num
    
    def deposit(self, amount):
        if (amount < 0):
            raise InvalidAmountException
        self._balance += amount
        print("The Deposit u made is successful! New balance:", self._balance)
    
    def withdraw(self, amount):
        if (amount < 0):
            raise InvalidAmountException
        if (amount > self._balance):
            raise ValueError
        self._balance -= amount
        print("The Withdraw u made is successful! New balance:", self._balance)

    def setBalance(self, balance):
        self._balance = balance

    def setName(self, name):
        self.__name = name

    def setAccountNum(self, acc_num):
        self.__acc_num =  acc_num
    
    def getBalance(self):
        return self._balance

    def getName(self):
        return  self.__name

    def setAccountNum(self):
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
    a.deposit(18)
    a.withdraw(200)
except ValueError:
    print("There is a value error occured!")
except InvalidAmountException:
    print("There is an invalid amount exception occured.")
except:
    print("There are other error!")
finally:
    print("congratulations!")

