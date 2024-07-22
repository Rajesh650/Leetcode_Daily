# class under class

class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap1 = self.laptop()

    class laptop():

        def __init__(self):
            self.brand = 'Apple'
            self.ram = '8gb'




s1 = student("Rajesh",23)
s2 = student("Paji",34)

print(s1.lap1.brand)
print(s2.lap1.brand)
print(s1.__dict__)

"""
you can create object of inner class
inside the outer class.

                    or

you can create object of inner class
outside the outer class provided you use
outer class name to call it.

"""