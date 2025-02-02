#These are the answers to the programming questions in Module 1 of the June 2022 Programming in Python Exam paper.
"""#Qn1) 
print(9/2)
print(9//2)
"""

"""#Qn2)
set = {1,2,3,4,5,6,7,8,9,11}
even=0
odd=0
print("Length of Set:",len(set))
for i in set:
    if (i%2==0):
        even=even+1
    else:
        odd=odd+1

print("The number of odd numbers in the set is: ",odd)
print("The number of even numbers in the set is: ",even)
"""

"""#Qn11a)
limit = int(input("Enter the number of rows: "))
for i in range(1,limit+1,1):
    for j in range(1,i+1,1):
        
        print(j," ",end="")
    j=0
    print("\n")
"""

"""#Qn12a)
count=0;
for num in range(0,1000,1):
    for j in range(1,num+1,1):
        if (num%j)==0:
            count=count+1;
        
    if (count==2):
        print(num)
    count=0
"""
#Qn12b)
import math
x1=int(input("Enter the initial x-coordinate: "))
y1=int(input("Enter the initial y-coordinate: "))

x2=int(input("Enter the final x-coordinate: "))
y2=int(input("Enter the final y-coordinate: "))

dx=(x2-x1)**2
dy=(y2-y1)**2
ans=math.sqrt(dx+dy)
print("The distance between the 2 points is: ",ans)
