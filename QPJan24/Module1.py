# Write a program that accepts the lengths of three sides of a triangle as inputs and outputs whether or not the triangle is a right triangle.
"""
import math

s1 = 3
s2 =4
s3 = 5

if(s3==math.sqrt(s1**2 + s2**2)):
    print("True")

else:
    print("False")
"""

# Write a Python program to print all numbers between 100 and 1000 whose sum of digits is divisible by 9.

"""
for i in range (100,1000):
    temp=i
    sum=0
    while(temp>0):
        dig=temp%10
        sum=sum+dig
        temp=temp/10
    if(sum%10==0):
        print(i)

"""

# Write a Python program to print all prime factors of a given number.
"""
num=60
fac=[]
def prime(num):
    while(num%2==0):
        fac.append(2)
        num=num/2

    i=3
    while(i*i<=num):
        while (num%i==0):
            fac.append(i)
            num=num/i
        i=i+2

    if num>2:
        fac.append(num)

    return fac

ans = prime(num)
print(ans)
"""