"""
f1=open("test.txt","w")
f1.write("Learning files now!")


def files(text):
    f1=open("test1.txt","w")
    f1.write(text)


files("Hello")



word = [13,100]


def sq(x):
    return x*x

ans = map(sq,word)
print(ans)

"""
from functools import reduce
num =[11,20,30,40,43]

def fil(x,y):
    return x+y
        
    
ans=reduce(fil,num)

print(ans)