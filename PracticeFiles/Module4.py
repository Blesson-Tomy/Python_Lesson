'''
class Student:
    

    def __init__(self,rollno,balance):
        self.rollno=rollno
        self.__balance = balance
        

    def read_dets(self,name,age,section):
        self.name=name
        self.age=age
        self.section=section
    
    def print_dets(self):
        print("Name is: ",self.name)
        print("Age is: ",self.age)
        print("Branch is:",self.section)

    def set_deets(self,name,age,section):
        self.name=name
        self.age=age
        self.section=section
    
    def get_deets(self):
        print("Name is: ",self.name)
        print("Age is: ",self.age)
        print("Branch is:",self.section)
    
    def accessor(self):
        print(self.__balance)
    
    def mutator(self,name,balance):
        self.name=name
        self.__balance=balance

    


s1= Student(1)
s1.read_dets('Blesson',22,'CSE-B')

s2= Student(2)
s2.read_dets('Joel',21,'ECS')

print("The student details are as follows.......... ")
print(f"The details of rollno {s1.rollno}.")
s1.print_dets()
print(f"The details of rollno {s2.rollno}.")
s2.print_dets()

s1.get_deets()



#super function()

class parent():
    def __init__(self,name):
        self.name=name
        print("This is the parent")
    
    def read_dets(self,name,age,section):
        self.name=name
        self.age=age
        self.section=section
    
    def print_dets(self):
        print("Name is: ",self.name)
        print("Age is: ",self.age)
        print("Branch is:",self.section)

class child(parent):
    def __init__(self,name):
        super().__init__(name)

    def read_dets(self,name,age,section):
        super().read_dets(name,age,section)
    
    def print_dets(self):
        super().print_dets()


c1=child('Blesson')
c1.read_dets('Blesson',89,'CSE')
c1.print_dets()




class oper():

    def operation(self,a=None,b=None):
        if(a!=None and b!=None):
            print(a*b)
        elif(a!=None):
            print(a*a)
        else:
            print("error")
o=oper()

o.operation(10,20)
o.operation(10)
o.operation()




class Parent:

    def hi(self,name):
        print("This is the parent")

class Child(Parent):

    def hi(self,name):
        print("This is the child")

s1=Parent()
s2=Child()

s1.hi('Blesson')
s2.hi("Blesson")



from abc import ABC, abstractmethod

class abs(ABC):

    @abstractmethod
    def hi(self):
        None
    
    def hello(self):
        print("Blesson")

class absc(abs):
    def hi(self):
        print("Is this abstract class working correctly?")


'''

try:
    a=10
    b=20
    c=30
    ans=a/0.05
    print(a)
    if(a<4):
        raise ZeroDivisionError
    else:
        print("All good")
except ZeroDivisionError:
    print("Error encountered")
else:
    print("ELSE BLOCK: No errors ")

finally:
    print("FINALLY BLOCK:")