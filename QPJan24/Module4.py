#18a) Different types of inheritance: Single, Multilevel, Multiple, Hierarchial, Hybrid

#Qn18b) Write a Python program to demonstrate the use of try, except and finally blocks
"""
class HelloError(Exception):
    pass

a=10
b=20
c=0

try:
    ans=a/b

    if(a<15):
        raise HelloError("Whoops")


except ZeroDivisionError:
    print("Cannot divide a number by o")

except HelloError as e:
    print("Caueght",e)

else:
    print("Done")

finally:
    print("Program savely continued")

"""

#Qn17a) Illustrate the use of Abstract Classes in Python

from abc import ABC,abstractmethod

class absc(ABC):

    @abstractmethod
    def legs(self):
        pass

    def hands(self,num):
        self.num=num
        print("I have hands ",self.num)

class cat(absc):
    def legs(self,num):
        self.num=num
        print("I have legs ",self.num)
    def hands(self,num):
        self.num=num
        print("I have hands ",self.num)

c=cat()
c.hands(10)
a=absc()
a.hands(3)
