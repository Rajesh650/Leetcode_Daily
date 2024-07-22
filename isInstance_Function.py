class demo :
    pass

d1 = demo()

class emp :

    def __init__(self,name ,age):

        self.name = name
        self.age = age

emp1 = emp("Rajes",24)
print(isinstance(emp1,emp)) 
print(isinstance(emp1,demo))
#isinstance() returns boolean value if object is a part of class then it will return true otherwise false