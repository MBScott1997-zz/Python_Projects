'''
Python Project - Marvel Mart Project
Michael Scott
Due: March 10, 2020
'''

import csv
import numpy as np
import pandas as pd
import collections
from collections import defaultdict

pd.set_option('display.float_format', lambda x: '%.3f' % x)

#Part 1: Cleaning the data
#Cleaning ints out of Country
mart = pd.read_csv('DataSamples/Marvel_Mart_Sales_clean.csv', delimiter=',')

for index, row in mart.iterrows():
    try:
        result = float(row.loc["Country"]) #if it can be converted to a float that's bad
        mart.loc[float(index), "Country"] = "NULL" #so change it to null
    except:
        1==1

#cleaning blanks out of item type & priority
mart["Item Type"].fillna("NULL", inplace=True) #fill blanks with null
mart["Order Priority"].fillna("NULL", inplace=True) #fill blanks with null

#cleaning strings from order id
for index, row in mart.iterrows():
    try:
        placeholder = row.loc["Order ID"] * 2 #if it can be multiplied by two that's good
    except:
        mart.loc[int(index), 'Order ID'] = 0 #if it can't change it to zero

# Part 2: General Statistics
#1A
print("\n-2.A-")
print("Countries Most Sales:")
data = mart.groupby(["Country"],sort=True)["Units Sold"].sum().reset_index() #group by country and sum units sold
data = data.sort_values(by = ['Units Sold'], ascending=[False]) #sort units sold sums
topTenSales = data.head(10) #top ten values

print(topTenSales)
print("\nThe country we should build our shipping center is Cape Verde because they are our third biggest customer by Units Sold")
      
#1B
print("\n-2.1.B-")

offline = collections.Counter() #counter variable
with open('DataSamples/Marvel_Mart_Sales_clean.csv') as input_file: 
    for row in csv.reader(input_file, delimiter=','): 
        offline[row[3]] += 1 #everytime "offline" is in row[3] count it
print('Number of offline sales: %s' % offline['Offline']) 

online = collections.Counter() #counter variable
with open('DataSamples/Marvel_Mart_Sales_clean.csv') as input_file:
    for row in csv.reader(input_file, delimiter=','):
        online[row[3]] += 1 #everytime "online" is in row[3] count it
print('Number of online sales: %s' % online['Online'])

if online['Online'] > offline['Offline']: #if more online sales
    print("We have more online sales") #print there's more online sales
else:
    print("We have more offline sales") #if not, tell us there's more offline sales
    
#C 
print("\n-2.1.C-")

mart['year'] = pd.DatetimeIndex(mart['Order Date']).year #adding a year column to make the rest easier

print("Best Years:")
data = mart.groupby(["year"],sort=True)["Total Profit"].sum().reset_index() #group by year and sum total profits
data = data.sort_values(by = ['Total Profit'], ascending=[False]) #sort total profit desc
data1 = data.head(3) #top 3 values
print(data1)

print("\nWorst Years:")
data = mart.groupby(["year"],sort=True)["Total Profit"].sum().reset_index() #group by year and sum total profits
data = data.sort_values(by = ['Total Profit'], ascending=[True]) #sort total profit asc
data2 = data.head(3) #top (bottom) three values
print(data2)

print("\nWe sold the most in 2011")

with open('DataSamples/Marvel_Mart_Rankings.txt', 'w+') as reader:
    reader.write("-2.A-")
    reader.write("\nCountries Most Sales: ")
    reader.write("\n")
    topTenSales.to_string(reader)
    reader.write("\n")
    reader.write("\nThe country we should build our shipping center is Cape Verde because they are our third biggest customer by Units Sold")
    reader.write("\n")
    reader.write("\n-2.1.B-")
    reader.write("\n")
    reader.writelines(str(onlinePrint))
    reader.write("\n")
    reader.writelines(str(offlinePrint))
    reader.write("\n")
    reader.write("We have more online sales")
    reader.write("\n")
    reader.write("\n-2.1.C-")
    reader.write("\n")
    data1.to_string(reader)
    reader.write("\n")
    reader.write("\n")
    data2.to_string(reader)
    reader.write("\n")
    reader.write("\nWe sold the most in 2011")
#making a nicely formatted .txt file :) 

#2A
print("\n-2.2.A-")

print("Sums:")

totalUnits = mart['Units Sold'].sum() #summing units sold
sum1 = "Units Sold: " + str(totalUnits) #print var
print(sum1)

totalUnits = mart['Unit Cost'].sum()
sum2 = "Unit Cost: " + str(totalUnits)
print(sum2)

totalUnits = mart['Total Revenue'].sum()
sum3 = "Total Revenue: " + str(totalUnits)
print(sum3)

totalUnits = mart['Total Cost'].sum()
sum4 = "Total Cost: " + str(totalUnits)
print(sum4)

totalUnits = mart['Total Profit'].sum()
sum5 = "Total Profit: " + str(totalUnits)
print(sum5)

print("\nAverages:")

totalUnits = mart['Units Sold'].mean() #averaging column
avg1 = "Units Sold: " + str(totalUnits) #print variable
print(avg1)

totalUnits = mart['Unit Cost'].mean()
avg2 = "Unit Cost: " + str(totalUnits)
print(avg2)

totalUnits = mart['Total Revenue'].mean()
avg3 = "Total Revenue: " + str(totalUnits)
print(avg3)

totalUnits = mart['Total Cost'].mean()
avg4 = "Total Cost: " + str(totalUnits)
print(avg4)

totalUnits = mart['Total Profit'].mean()
avg5 = "Total Profit: " + str(totalUnits)
print(avg5)

print("\nMaximums:")

totalUnits = mart['Units Sold'].max() #finding the max value from the column
max1 = "Units Sold: " + str(totalUnits) #print variable
print(max1)

totalUnits = mart['Unit Cost'].max()
max2 = "Unit Cost: " + str(totalUnits)
print(max2)

totalUnits = mart['Total Revenue'].max()
max3 = "Total Revenue: " + str(totalUnits)
print(max3)

totalUnits = mart['Total Cost'].max()
max4 = "Total Cost: " + str(totalUnits)
print(max4)

totalUnits = mart['Total Profit'].max()
max5 = "Total Profit: " + str(totalUnits)
print(max5)

with open('DataSamples/Marvel_Mart_Calc.txt', 'w+') as reader:
    reader.write("-3-")
    reader.write("\n")
    reader.write("Sum: ") 
    reader.write("\n")    
    reader.writelines(sum1)
    reader.write("\n")
    reader.writelines(sum2)
    reader.write("\n")
    reader.writelines(sum3)
    reader.write("\n")
    reader.writelines(sum4)
    reader.write("\n")
    reader.writelines(sum5)
    reader.write("\n")
    reader.write("Averages: ")
    reader.write("\n")    
    reader.writelines(avg1)
    reader.write("\n")
    reader.writelines(avg2)
    reader.write("\n")
    reader.writelines(avg3)
    reader.write("\n")
    reader.writelines(avg4)
    reader.write("\n")
    reader.writelines(avg5)
    reader.write("\n")
    reader.write("Maximums: ")
    reader.write("\n")
    reader.writelines(max1)
    reader.write("\n")
    reader.writelines(max2)
    reader.write("\n")
    reader.writelines(max3)
    reader.write("\n")
    reader.writelines(max4)
    reader.write("\n")
    reader.writelines(max5)
# making another nicely formatted .txt for you :) 
    
    
#Part 3: Cross-Reference Statistics
#1
print("\n-3.1.A")
dictOfLists = {} #empty dict
for i in mart.Region.unique(): #for each unique region
    dictOfLists[i] = mart[mart.Region == i].Country.unique().tolist() #put the corresponding unique country into a list and the list as a value to the region key

df=pd.DataFrame.from_dict(dictOfLists,orient='index').transpose() #dict to dataframe
df.to_csv('DataSamples/Countries_By_Region.csv', encoding='utf-8', index=False) #dataframe to csv

for i in dictOfLists: #printing the keys of the dict of lists
    print(i) #printing the regions line by line


    