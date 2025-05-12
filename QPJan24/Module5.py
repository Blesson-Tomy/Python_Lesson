# Qn19a) consider a csV file 'weather.csv' with the following columns (date,temperature, humidity, windSpeed, precipiJationType, prace, weather Cloudy, Sunny)).
#Write commands to do the following using pandas library.
#1. Print first l0 rows of weather data
#2. Find the maximum and minimum temperature 
# 3. List the places with temperature less than 28 degrees.,,
#4. List the places with weather = Cloudy
#5. Sort and display each weather and its frequency
#6. Create a bar plot to visualize temperature of each day.
"""
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd

data={
    'date': ['2022-10-22','2022-10-21','2022-10-20','2022-10-25'],
    'temperature':[10,20,30,40],
    "humidity": [1,2,3,4],
    "windspeed": [100,200,300,400],
    "precipitationtype": ["high","low","medium","low"],
    "place": ["up","down","asia","pacific"],
    "weather": ["cloudy","sunny","rainiy","cloudy"]
}



df=pd.DataFrame(data)
pd.to_datetime(df['date'])
df.to_csv("wind")


print("First 10 rows:",df.head())
print("Max and Min:",df["temperature"].max(),df["temperature"].min())
print("Locations:\n",df[df["temperature"]<28])
print("Cloudy Locations:\n",df[df["weather"]=="cloudy"])
ans=df['weather'].value_counts().sort_values(ascending=False)
print("Weather:\n",ans)

df.plot(kind="bar",x='date',y='temperature')
plt.show()

"""

#Qn20a) Write a pyhton program to write the data into a CSV File
"""
import pandas as pd

books={
    "sl": [1,2,3],
    "title": ['The great gatsby','Pride and Prejudice','The time machine'],
    "author": ['F Scott', 'JA','HG Wells'],
    "available": ['Y','Y','N'],
    "count": [20,15,0]
}

df=pd.DataFrame(books)
df.to_csv("Books.txt",index='False')

"""

#Qn20b) Write a python program to input two matrices and perform the following operations using numpy and display the results:
#1. Add the matrices
#2. Subtract the matrices
#3. Multiply the matrices
#4. Find transpose of the matrices
"""
import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])

b=np.array([[1,2,3],[4,5,6],[7,8,9]])

c=np.add(a,b)
print(c)
d=np.subtract(a,b)
print(d)
e=np.multiply(a,b)
print(e)
f=np.transpose(a)
print(f)

"""
