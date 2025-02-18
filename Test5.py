#Test Case 5
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def deposit(self, balance):
        self.balance = self.balance + balance
        return "Deposited " + str(balance) + ". New balance: " + str(self.balance)
    
    def withdraw(self, balance):
        flag = True if self.balance >= balance else False
        self.balance = (self.balance - balance) if self.balance >= balance else self.balance
        return "Withdrew " + str(balance) + ". New balance: " + str(self.balance) if flag else "Invalid withdrawal amount or insufficient funds"

account = BankAccount("Name")
print(account.deposit(1000))   
print(account.withdraw(500))   
print(account.withdraw(600))   