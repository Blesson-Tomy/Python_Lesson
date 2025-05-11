#11a) Write a python program to find the sum of the cosine series 

"""
import math
x=int(input("Enter the value of X:"))
n=int(input("Enter the value of limit:"))

ans=1
for i in range(2,n,2):
    ans=ans+((-1)**(i//2))*(x**i)/math.factorial(i)

print (ans)
"""

#11b) Write a PYthon Program to find X^Y or pow(X,Y) without using standard functions

"""
x=int(input("Enter the value of X:"))
y=int(input("Enter the value of Y:"))
ans=x
for i in range(1,y):
    ans=ans*x

print("The answer is",ans,"which is the same as",x**y,".")
"""

#12a) write a python program to generate the following type of pattern for rows where N <= 26.
"""
A
A B
A B C
A B C D


n=int(input("Enter the limit:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64)," ", end='')
    print("")

"""
#12b) Write a python program to generate prime numbers within a certain range

"""
up=int(input("Enter the upper limit: "))
down=int(input("Enter the lower limit: "))
count=0
for i in range(down,up+1):
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    
    if(count==2):
        print(i)
    count=0

"""