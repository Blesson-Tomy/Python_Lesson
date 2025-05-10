#These are the answers to the programming questions in Module 1 of the June 2022 Programming in Python Exam paper.
"""#Qn1) What is the output of the following statements?

Ans:
print(9/2)
print(9//2) 

"""



"""#Qn2) Python program to print the number of odd and even numbers in a given set of n numbers.

Ans:
n = int(input("Enter the value of n:"))
ecount=0
ocount=0
for i in range(n+1):
    if(i%2==0):
        ecount=ecount+1
    else:
        ocount=ocount+1

print("The number of Even Numbers is: ",ecount,".")
print("The number of Odd Numbers is: ",ocount,".")

"""


"""#Qn11a) Generate a pattern as shown below:
1
1 2
1 2 3
1 2 3 4

Ans:
num=5
for i in range(1,5+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
"""




"""#Qn12a) Python program to print all prime numbers less than 1000.

for i in range(1,1000):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1

    if(count==2):
        print(i)

"""


"""#Qn12b) Write a python program to find the distance between two points (x1,y1) and (x2,y2).

from math import sqrt
x1=20
x2=30
y1=50
y2=60
dist=sqrt((x2-x1)**2 + (y2-y1)**2)

"""

