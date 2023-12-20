class person:
    def ___int___ (self,name,age):
        self.name=name
        self.age=age
    def pp(self):
        self.m=self.name
    def oo(self):
        self.n=self.age
    def disp(self):
        print("name of the person",self.m)
        print("age is:",self.n)

        name=input("enter the name")
        age=int(input("enter the age"))
        obj1 = person(name,age)
        obj1.disp()