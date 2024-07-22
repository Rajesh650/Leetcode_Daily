# creating instance variable outside class

# class emp:

#     def __init__(self,name ,age):

#         self.name = name  #name and age is instance variable
#         self.age = age

# emp1 = emp("Raj",23)
# emp2 = emp("Ram",24)
# emp3 = emp("pooja",34)

# #outside the class

# emp1.age = 34
# print(emp1.__dict__)
# print(emp3.__dict__)

# del emp2.age
# print(emp2.__dict__)

# creating Instance method outside the class

class emp :


    company = "BMW" #class variable 
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
"""
    we can create n number of copies for instance variables 
    but for class variable we can create only one 1 variale. 

    class variable is always defined below class declaration and above method declaration
    so that class variable can be accessed all over the program


"""