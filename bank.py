class Bank(object):
    def __init__(self,atmnumber,pincode,balance):
        self.atmnumber = atmnumber
        self.pincode = pincode
        self.balance = balance
    def balanceEnquiry(self):
        moneyleft = str(self.balance)
        pin = input("Enter pincode to see balance: ")
        while pin != self.pincode:
            print("pincode is wrong")
            pin = input("Enter pincode: ")
        return("You have " + moneyleft + " left in your account")
    def withdrawal(self):
        pin = input("Enter pincode: ")
        while pin != self.pincode:
            print("pincode is wrong")
            pin = input("Enter pincode: ")
        withdraw = input("Enter amount to be withdrawn: ")
        cash = int(withdraw)
        self.balance = self.balance - cash
        moneyS = str(cash)
        return(moneyS + " has been withdrawn.")

john = Bank(123,"johnpin",100000)    

print(john.withdrawal())
print(john.balanceEnquiry())
