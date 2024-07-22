"""class human:

    def setName(self,name):

        self.Name = name

    def setGender(self,gender):

        self.Gender = gender

    def setAge(self,age):
        
        self.Age = age

    def getInformation(self):

        return  (self.Name+","+self.Gender+","+self.Age)
    
man1 = human()
# print(type(man1))

man1.setName("Raj")
man1.setGender("Male")
man1.setAge("24")

print(man1.getInformation())

man2 = human()
man2.setName("Rajesh")
man2.setGender("Male")
man2.setAge("24")

print(man2.getInformation())


class car :
    def setName(self,name):
        self.Name = name
    
    def setColour(self,colour):
        self.Colour = colour

    def setBrand(self,brand):
        self.Brand = brand

    def getInfo (self):
        return (self.Brand +","+ self.Colour+","+self.Name)
       
CAR1 = car()
CAR1.Brand = ("BMW")
CAR1.Colour =("WHITE")
CAR1.Name =("X700")
print(CAR1.getInfo())

class sevenWonders:

    def setName (self,name):
        self.Name = name

    def setName (self,location):
        self.Location = location

    def getInfo(self):
        return(self.Name+" is in "+self.Location)
    

sevenWonders1 =sevenWonders()

sevenWonders1.Name=("Taj Mahal")
sevenWonders1.Location=("India")

print(sevenWonders1.getInfo())"""


class Friends:

    def setname(self,name):
        self.Name = name

    def setage(self,age):
        self.Age = age

    def setmobileno(self,mobileno):
        self.Mobileno = mobileno

    def setlocation(self,location):
        self.Location = location

    def getinfo(self):
        return(self.Name +" "+self.Age+" "+self.Mobileno+" "+self.Location)

Friend1 = Friends()
Friend1.setname ("ABC")
Friend1.setage ("22")
Friend1.setmobileno ("XXXXXX")
Friend1.setlocation ("XYZ")
print(Friend1.getinfo())