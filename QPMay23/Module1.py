#Qn1) What is the output of the following Python code. Justify your answer.

"""
x='abcd'

for i in range(len(x)):
    print(i)
"""


#Qn11a) Write a Python program to find the roots of a quadratic equation, ax * bx * c:0 . Consider the cases of both real and imaginary roots.

"""
import cmath 
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))

real=(-b+cmath.sqrt((b**2)-(4*a*c)))/(2*a)
img = (-b-cmath.sqrt(b**2-4*a*c))/(2*a)

print(f"The answer is{real}+{img}i")
"""

#Qn11b) Write a Python program to check whether a number is Armstrong number or not. An Armstrong number is an n-digit number that is equal to the sum of the n powers of its digits.

"""
store=num = int(input("Enter the number: "))
len1=int(len(str(abs(num))))
sum1=0
while(num>0):
    temp=num%10
    sum1=(temp**len1)+sum1
    num=num//10

if (sum1==store):
    print("It is an armstrong number.")
else:
    print("It is not an armstrong number.")
"""

#12a) Write a Python program to display the sum of odd numbers between a programmer specified upper and lower limit.

"""
up=int(input("Enter the upper limit: "))
down=int(input("Enter the lower limit: "))
res=0
for i in range(down,up+1):
    if(i%2==1):
        res=res+i

print("The answer is",res)
"""

#12b) Given the value of x, write a Python program to evaluate the following series upto n terms:

"""
import math
n=int(input("Enter the limit:"))
x=int(input("Enter the limit of X:"))
sum=1
for i in range(1,n+1):
    sum=(x**i)/math.factorial(i)+sum

print("The answer is:",sum)
"""
