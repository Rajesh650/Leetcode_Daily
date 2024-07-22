"""
we have three types of methods:-
1.class method     // it is defined outside the __init__()method and we use @classmethod to access and it deals with only class variable
2.static method    //it defined in inside __init__() method and we use @staticmethod to access and it have nothing to deal with class and instance methods
3.Instance method   // it have to deal with only Instance variable and we can access it without any decorators
"""

class student:

    school = 'ABC'

    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def avg(self):
        return (self.m1+self.m2)/2
        
    @classmethod

    def get_info(cls):
        return cls.school
        
    @staticmethod
    def info():
        print("this is in abc  class")

s1 = student(22,22)
s2 = student(20,20)

print(s1.avg())
print(student.get_info())

student.info()


