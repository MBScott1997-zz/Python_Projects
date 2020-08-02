'''

Python Lab #6

Michael Scott

'''

import numpy as np
import pandas as pd
import statistics as st

# 1
print("\n-1-")

planets = np.array([["Mercury", "Venus", "Mars"], ["Jupiter", "Saturn", "Uranus"], ["Pluto"]])

print(planets)

# 2
print("\n-2-")
#creating an array
planets = np.array([["Mercury", "Venus", "Mars"], ["Jupiter", "Saturn", "Uranus"], ["Pluto"]])
#printing the 1st of the 3 arrays, and the 2nd value from that chosen array
print(planets[0][1] + " is the second planet from the sun.\n")
#printing the 3rd of the 3 arrays, and the 1st value from that chosen array
print(planets[2][0] + " is not a planet... :(")

# 3
print("\n-3- help")
#array with 10 to 100 by 10
arr = np.array([10,20,30,40,50,60,70,80,90,100])
#from 4th to 9th by 2
sub1 = arr[3:8:2]
#from 1st to 6th by 2
sub2 = arr[0:5:2]

product = np.multiply(sub1, sub2) #multiply
print(product) #print

# 4
print("\n-4-")
#creating the two lists
classes = ["Algebra I", "Intro to Business", "Creative Writing"]
students = [30, 31, 29]
#creating a pandas Series with the students as values and classes as index
att = pd.Series(students, classes)
#adding an index and value
att["Programming"] = 31
print(att) #print the entire series
print("\n")
print(att[att<31]) #print only when the value is < 31

# 5
print("\n-5-")
#creating the data dictionary
data = {"Test 1": [92, 72, 98], "Test 2":[85, 83, 89], "Test 3": [83, 99, 61]}
#creating a dataframe using the data dictionary and adding names as indexes
df = pd.DataFrame(data, index=["Sean", "Claude", "Laura"])
print(df) #printing the whole dataframe
print("\n")

df.loc["Claude"]["Test 2"] = '81' #changing [Claudes] [2nd test score] to 81
df.loc["James"] = [72, 83, 99] #adding james's score from tests 1-3 
df["Test 4"] = [69, 71, 72, 83] #adding everybody's test 4 score
print(df)

# 6
print("\n-6-")
#creating a dictionary with sales numbers per phone
salesDict = {'Samsung Galaxy S10': [769.34, 834.23, 900.12, 1021.12],
'iPhone X': [983.11, 881.21, 1210.32, 1100.34],
'Google Pixel 4': [1021.18, 1321.12, 832.14, 992.15]}
#list with dates of sales
dates = ['01/01/2020', '01/02/2020', '01/03/2020', '01/04/2020']

sales = pd.DataFrame(salesDict, dates) #dataframe using the dates as indexes and the data dictionary as column names and values
print(sales)
print("\n")
 
sales["Mean"] = sales.mean(axis = 1) #adding means of each row
sales["Median"] = sales.median(axis = 1) #adding medians for each row
sales["St Dev"] = sales.std(axis = 1) #adding standard deviations for each row

sales = sales.drop("Samsung Galaxy S10", axis = 1) #dropping the phone columns
sales = sales.drop("iPhone X", axis = 1)
sales = sales.drop("Google Pixel 4", axis = 1)

print(sales) #print
