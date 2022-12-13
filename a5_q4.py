class Account:
    def __init__(self,title=0, Balance=0):
        self.title=title
        self.Balance=Balance
        

class SavingsAccount(Account):
    def __init__(self, title=0 , Balance=0, intrestRate=0):
        super().__init__(title,Balance)
        self.intresrRate=intrestRate

obj1=Account("Ashish", 5000)
print(f"\n  Name of the account holder :{obj1.title} , \n Account balance: {obj1.Balance}")
obj2=SavingsAccount ("ashish",5000,5)
print(f"\n  Name of the account holder :{obj1.title} , \n Account balance: {obj1.Balance}, \n interest: {obj2.intresrRate}")


     