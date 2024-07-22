class emp :
    
    company = "BMW"                  
    #class variable 
    def __init__(self,name ,age):

        self.name = name
        self.age = age

    def display(self):
        print(self.name ,self.age)

    def change_data(self):
        self.name = 'abc'
        self.age = 234
        # print(self.name ,self.age)

emp1 = emp('Raj',33)
emp2 = emp('Ram',22)

# creating instance method outside the class

emp1.display()

emp2.change_data()

# print(emp.company)
# print(emp1.company)

emp.company = "Google"

# print(emp2.company)
print(emp.company)
# print(emp1.company)

# print(emp2.__dict__)
print(emp1.__dict__)
emp1.company = 'Microsoft'
print(emp2.company)

print(emp1.__dict__)