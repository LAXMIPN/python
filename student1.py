class student:
   def __init__(self,n,i,m):
       self.n=n
       self.i=i
       self.m=m


n=input("enter the name:")
i=int(input("enter the id:"))
m=int(input("enter the mark:"))
obj1=student(n,i,m)
print(obj1.i)
print(obj1.m)
print(obj1.n)