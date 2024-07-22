class emp:

    def setname(self,name):
        self.name= name

    def getname(self):
        print("the name is ",self.name)

emp1 = emp()
emp2 = emp()

emp1.setname(input("enter your name:-"))
emp2.setname(input("enter your name:-"))

print(emp1.__dict__)
print(emp2.__dict__)