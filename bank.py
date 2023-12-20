class bank:
    def __init__(self,a,n,b,t):
        self.accountnumber=a
        self.name=n
        self.type=t
        self.balance=b
    def depo(self, a1):
            self.balance +=a1
            print("balance:",self.balance)

    def w(self,a2):
           if self.balance<a2:
               print("invalid")
           else:
               self.balance -=a2
               print("balance:",self.balance)
    def dis(self):
            print(" the acc no:",self.accountnumber)
            print(" the name",self.name)
            print(" the type of account:",self.type)
            print("balance :",self.balance)

a=int(input("enter the acc no:"))
n=input("enter the name:")
t=input("enter the type of acc:")
b=int(input("enter the acc balance"))
obj1=bank(a,n,t,b)
obj1.dis()
a1 = int(input("Enter the amount to deposite:"))
obj1.depo(a1)
a2 = int(input("Enter the amount to widthdraw:"))
obj1.w(a2)











