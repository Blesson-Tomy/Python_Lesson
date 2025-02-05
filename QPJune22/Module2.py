#These are the answers to the programming questions in Module 1 of the June 2022 Programming in Python Exam paper.
""" #Qn4) Create a file and write a string into it. Then read and print the string.
print("Creating a file.....\n")
f1=open("file1.txt","w")
print("Writing to the file.....\n")
f1.write("Welcome to python programming\n")
print("Reading from the file.....\n")
f1=open("file1.txt","r")
text=f1.read()
print(text)
"""

""" #Qn13a) Write a python program to count how many times each character appears in a given string and store the count in a dictionary with key as the character.
strin="All the best CSE-B"
dic={}

for i in strin:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]=dic[i]+1

print(dic)
"""

""" #Qn13b) Create a funtion min_max() that takes n numbers as list argument and return the smallest and largest numbers.
def min_max(listt):
    minn=11110
    maxx=0
    for num in listt:
        if num>maxx:
            maxx=num
        if num<minn:
           minn=num
    
    print(minn)
    print(maxx)

listt=[10,20,30,40]
min_max(listt)
"""

""" #Qn14a) Python program to read n numbers into a list and separate the positive and negative numbers into 2 different lists.
n=int(input("Enter the limit of the numbers:"))
lis=[]
for i in range(0,n):
    num=int(input("Enter the number:"))
    lis.append(num)
print(lis)
pos=[]
neg=[]
for i in lis:
    if(i>0):
        pos.append(i)
    else:
        neg.append(i)
print(pos)
print(neg)
"""

""" #Qn14b) Create a dictionary of names and birthdays. Write a python program that asks the user to enter a name and the program displays the birthday.
db={"Blesson":"10-10-2025","Binil":"09-09-2027","Aromal":"10-20-2004"}
query=input("Whose birthday would you like to know?")
ans=db.get(query)
print(ans)
"""