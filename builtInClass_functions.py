class emp:

    def __init__(self,name,age):

        self.name = name
        self.age = age

emp1 = emp("Rajesh",24)
emp2 = emp("Ramesh",25)
# print(getattr(emp1,"age"))  #getMethod:- to get the value from object
# print(getattr(emp2,"name"))
setattr(emp1,"name","Rajesh Singh")  #setattr is used to set the value of an object
print(getattr(emp1,"name"))

delattr(emp2,"name")    #delattr is used to delete the object value 
# print(getattr(emp2,"name"))
