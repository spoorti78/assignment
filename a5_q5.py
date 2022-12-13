class Account:
    def __init__(self, title=None, account_balance=0):
        self.title = title
        self.account_balance = account_balance
    
    def withdrawal(self, amount):
        self.amount = amount
        self.account_balance = self.account_balance - self.amount

    def deposit(self, amount):
        self.amount = amount
        self.account_balance = self.account_balance + self.amount
    def getBalance(self):
        return self.account_balance

class SavingsAccount(Account):
    def __init__(self, title=None, account_balance=0, interestRate=0):
            super().__init__(title, account_balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.account_balance * self.interestRate / 100 ) 
        

savingsaccount = SavingsAccount("spoorti",10000,5)
print("Initial Balance : ",savingsaccount.getBalance())
savingsaccount.withdrawal(500)
print("Balance after withdrawal : ",savingsaccount.getBalance())
savingsaccount.deposit(1500)
print("After deposit : ",savingsaccount.getBalance())
print("Intrest on current balance : ",savingsaccount.interestAmount())