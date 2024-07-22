class A:
    def feature1(self):
        print("Feature1 is working")

    def feature2(self):
        print("Feature2 is working")

class B:
    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")

class C(A, B):
    def feature5(self):
        print("Feature5 is working")

# Creating an instance of class C
c_instance = C()

# Calling methods
c_instance.feature1()  # Output: Feature1 is working
c_instance.feature2()  # Output: Feature2 is working
c_instance.feature3()  # Output: Feature3 is working
c_instance.feature4()  # Output: Feature4 is working
c_instance.feature5()  # Output: Feature5 is working
