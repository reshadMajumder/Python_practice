class Account():
    def __init__(self, accNo, balance):
        self.accNo = accNo
        self.balance = balance


    def credit (self,amount):
        self.balance += amount
    def debit(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
        
    def bal(self):
        print("available balance : " , self.balance)




a1=Account(101010,200)

a1.bal()
a1.credit(100)
a1.bal()
a1.debit(50)
a1.bal()