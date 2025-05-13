#Qn4) Write a program to identify palindromic words in lines of text.
"""
def pal(word):
    word=word.lower()
    return word==word[::-1]

f1=open("books.txt","r+")

f=f1.read()

f=f.split()
palindrome=set()

for word in f:
    word=''.join(filter(str.isalpha,word))
    if len(word)>1 and pal(word):
        palindrome.add(word)

for i in sorted(palindrome):
    print(i)
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


import os

ans=os.path.exists("Hello.gif")
print(ans)