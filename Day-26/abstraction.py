from abc import ABC,abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("You can checkout your balance")

    def viewhistroy(self):
        print("You can check your transactions")
        
    def userinfo(self):
        print("You can see your details")

    def transactions(self):
        print("You can transfer money through netbanking")

    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass


class CurrentAccount(BankAccount):
    def deposit(self):
        print("You can deposit -CA")
    def withdraw(self):
        print("You can withdraw-CA")

class SavingAccount(BankAccount):
    def deposit(self):
        print("You can deposit -SA")
    def withdraw(self):
        print("You can withdraw-SA")

class FixedDeposit(BankAccount):
    def deposit(self):
        print("You can deposit -FD")
    def withdraw(self):
        print("You can withdraw-FD")


class SalaryAccount(BankAccount):
    def deposit(self):
        print("You can deposit -SA")
    def withdraw(self):
        print("You can withdraw-SA")


class ZeroBalanceAccount(BankAccount):
    def deposit(self):
        print("You can deposit -ZBA")
    def withdraw(self):
        print("You can withdraw-ZBA")

praveen=ZeroBalanceAccount()
praveen.deposit()
praveen.withdraw()
praveen.userinfo()
praveen.viewhistroy()
praveen.transactions()


'''

You can deposit -ZBA
You can withdraw-ZBA
You can see your details
You can check your transactions
You can transfer money through netbanking

'''













    
