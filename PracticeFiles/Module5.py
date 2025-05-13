"""
f=open('sup.txt',"w+")
print(f.mode)
print(f.name)

print(f.closed)

try:
    f.write("This is the 5th module and I am feeling very sleepy,\n"
            "but the exam is tomorrow, so you have to stay focused and study!\n")

except:
    print("Written unsuccessfully")

else:
    print("Written successfully")

f.seek(0)
print(f.readlines())
with open('sup.txt',"r+") as f:
    for line ,text in enumerate(f):
        
        print(f"{line}: {text}")




import numpy as np

a = np.array([1,2,3,9,10,11,12,13])
b=np.array([[4,5,6],[7,8,9]])
c1=np.transpose(b)
c=np.random.choice(a)
print(c)



import matplotlib.pyplot as plt

year=[2000,2001,2002,2003,2004,2005,2006,2007]
run=[10,5,9,3,5,11,6,6]

run1=[35,5,13,34,25,11,26,16]

plt.title("Grid")
plt.plot(year,run,'b-x',label='us')
plt.plot(year,run1,'y-o',label='in')
plt.xlabel="year"
plt.ylabel="run"

plt.legend()
plt.show() 


import matplotlib.pyplot as plt 
import numpy as np

years=np.array([2000,2010,2020,2030])
econ=np.array([32,44,65,39])
econs=np.array([39,41,69,81])
plt.title("The Economic Growth")

plt.pie(econ,labels=years)
#plt.bar(years,econs,label="woo")
plt.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.random.normal(270,50,250)
plt.hist(x)
plt.show()

"""
"""
import pandas as pd
#import m#plotlib.pyplot as plt

data={
    'Reg No': ["ABC123","ECH265","FET345","GMT734"],
    'Name': ["Ganesh Kumar", "John Mathew", "Reena K","Adil M"],
    'Semester': ['S8','S7','S6','S5'],
    'College': ['ABC',"ECH","FET","GMT"],
    'CGPA': [9.8,9.9,9.7,9.75]
}

df=pd.DataFrame(data)
usecols=['Name','Semester']
df.to_csv("Data.csv",index=True)
ans=pd.read_csv("Data.csv",index_col=0,usecols=usecols)

#df.plot(kind='scatter')
#plt.show()

print("Checj",df['Name'].str.upper())


df[['column1', 'column2']] → selects columns.

df[df['column'] == value] → selects rows based on a condition.

df[df['column'].isin([...])] → selects rows where a column’s value is in a list.

print(df)

print("Avg:",df['CGPA'].mean())
print("Avg:",df[df['CGPA']>9])
print("CSE",df[(df["CGPA"]>9) & (df["Semester"]=='S8')])
print("Max",df[df["CGPA"]==df["CGPA"].max()])
"""

import numpy as np

x=np.random.randn(10)
print(x)

x1=x.reshape((1,10))
x1[x1<1]=0
print(x1)