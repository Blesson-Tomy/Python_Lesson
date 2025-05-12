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
"""
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
"""

#Qn17b) Define a class Student .
"""
class Student():
    rollno=0
    name=''
    math=0
    sci=0
    el=0

    def ReadD(self,rollno,name,math,sci,el):
        self.rollno=rollno
        self.name=name
        self.math=math
        self.sci=sci
        self.el=el

    def compute(self):
        tmarks=self.math+self.sci+self.el
        print(tmarks)
    
    def printt(self):
        print(self.rollno, self.name,self.math,self.sci,self.el,)


a=Student()
a.ReadD(11,'Blesson',100,100,99)
a.printt()

"""

#Qn14a) Decimal Number to binary equivalent
"""
dec=int(123)
res=''

while dec!=0:
    temp=dec%2
    res=str(temp)+res
    dec=dec//2

print(res)
"""

#14b) Read from file and count occurances and store into a dictionary
"""
f1=open("books.txt","r+")
dicti={}
f=f1.readlines()
for line in f:
    for ch in line.upper():
        if ch in dicti:
            dicti[ch]=dicti[ch]+1
        else:
            dicti[ch]=1

print(dicti)
"""

