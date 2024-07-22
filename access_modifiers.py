
# Access modifiers

class employee:

    def __init__(self,sal,age):

        self.sal = sal
        self.age = age

    def display(self):
        print(f"employee sal is {self.sal} and employee age is {self.age}")

emp1 = employee(23000,23)
emp2 = employee(25000,25)
# emp1.display()
print(emp1.sal)
# emp2.display()
print(emp2.age)