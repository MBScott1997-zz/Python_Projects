'''

Python Lab #4

Michael Scott

'''

# 1

print("\n-1-")
#creating the list
stateList = ["Washington", "Oregon", "California", "Nevada"]
stateList[3] = "Idaho" #changing nevada to idaho

print(stateList) #printing the list

# 2
print("\n-2-")
#creating the list
chars = ["Leslie", "Tom", "Ron"]
#printing each concat for each item in the list
for name in chars:
    print(name + " is a character on Parks and Rec")
    
# 3
print("\n-3-")

import random #importing random 
numList = [] #making an empty list
for i in range(0,10): #do this 10 times
    numList.append(random.randint(1,10)) #find a random number and add it to the list

for i in numList: #go through each number in the list
    if i % 3 == 0: #if it's divisible by 3
        print(i) #print it
        
# 4
print("\n-4-")

def holList(list1, list2):
    holidays = list1 + list2
    for newHoliday in holidays:
        if newHoliday != "Black Friday":
            print(newHoliday)

holidayOne = ["New Years Day", "Easter", "Fourth of July"]
holidayTwo = ["Halloween", "Thanksgiving", "Black Friday", "Christmas"]

holList(holidayOne, holidayTwo)

# 5
print("\n-5-")

cities = ["New York", "Los Angeles"] #OG list

cities.append("Miami") #append miami to front
cities.append("Houston") #append houston to front
cities.insert(0, "Seattle") #insert seattle to front
cities.insert(2, "Boise") #insert boise 3rd
del cities[0] #deleting first thing (Seattle)

print(cities) #print

# 6
print("\n-6-")

months = [["January", 31],["February", 29],["March", 31],["April", 30],["May", 31],["June", 30]]
i = 0 #creating a variable to help count
for i in months: #for each variable(month)
    monthName = i[0] #month name is just the 1st thing in each tuple
    monthDay = i[1] #month day is the 2nd in each tuple
    
    print(monthName, "has", str(monthDay), "days") #print

# 7
print("\n-7-")
#making the dictionary
dog = {"Breed":"Corgi","Age Exp.":13,"Type":"Cattle herding"}
#printing the stuff by calling the created indexes
print("The " + dog["Breed"] + " is expected to live about " + str(dog["Age Exp."]) + " years")    

# 8
print("\n-8-")

scores = {"Jeff":90,"Chris":59,"Hannah":88,"Michelle":99}

def addChangeScore(name, score): #creating the function addChangeScore
    scores[name] = score #adding names and scores

def delScore(name): #creating delScore function
    del scores[name] #deleting the score based on the name

addChangeScore("Joel", 78) #adding joel:78
addChangeScore("Joel", 79) #changing to joel:79
delScore("Hannah") #deleting hannah

for n,s in scores.items(): #for each n(ame), s(core)
    print(n + ": " + str(s)) #print them 
    
# 9
print("\n-9-")

names = ["Jasper", "Sam", "Meredith", "Chris"]
ages = [23, 28, 20, 30]

dict = {}

for n in names:
    dict[n] = {}
    for a in ages:
        dict[n] = a
    
for n,a in dict.items():
    print(n + ": " + str(a)) 

# 10
print("\n-10-")

scores = {"Jeff":90,"Chris":59,"Hannah":88,"Michelle":99} #scores dictionary
i = 0
for n,s in scores.items(): #for each index and value
    if int(s) >= 60: #if score over 60
        print(n + " passed the test") #print the name
    else: 
        print(n + " did not pass the test") #or.. still print the name
