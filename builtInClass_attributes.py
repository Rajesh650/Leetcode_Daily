class emp:
    '''This is about employee name and age'''

    def __init__(self,name,age):

        self.name = name
        self.age = age

emp1 = emp("Rajesh",24)
# print(emp1.name)
# print(emp.__doc__) #__doc__ attribute tells us about the pourpose of the program so we have to mention that pourpose otherwise we will get "none"

print(emp.__dict__)

print(emp.__base__) # <class 'object'>

print(emp.__name__) #emp