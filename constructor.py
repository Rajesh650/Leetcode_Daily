# there are three types of constructor

# 1. default constructor
# 2. parametrized constructor
# 3. non- parametrized constructor

# 1...........default constructor........

class emp:
    pass

e1 = emp()

# 2. parametrized constructor

class stu:
    def __init__(self,name,age):

        self.name = name
        self.age = age
stu1 = stu("Raj",24)
stu1 = stu("Rajesh",24)

# print(stu1.name + str(stu1.age))

# 3. non-parametrized constructor

class emp1:

    def __init__(self) :

        self.name = "Raj"
        self.age = 34

e1 = emp1()
# print(e1.name + str(e1.age))




