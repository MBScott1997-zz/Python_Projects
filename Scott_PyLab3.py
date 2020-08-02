'''

Python Lab #3

Michael Scott

'''

# 1
print("\n-1-")

stanLee = "Excelsior!" #creating the variable
print(stanLee[1]) #printing just the 2nd character (since it starts at 0)
print(stanLee[9]) #printing the 10th character (")

# 2
print("\n-2-")

callToAction = "Avengers Assemble"

for letter in callToAction: #for each new letter
    print(letter) #print it individually
print("!") #end with a !

# 3
print("\n-3-")

school = "Hogwarts"

first = school[0:3] #returning the first 3 characters (not including index 3)
second = school[3:8] #returning the last 5 characters 

print(first)
print(second) 
print(school[-1]) #printing the last character

# 4
print("\n-4-")

houses = ("Hufflepuff", "Gryffindor", "Ravenclaw", "Slytherin")
# created the tuple with house names
for house in houses: #for each individual house in the tuple
    print(house) #print each one
    
# 5
print("\n-5-")

rB = ("Red", "Blue") #tuple 1
gY = ("Green", "Yellow") #tuple 2
combo = rB + gY #concatenate tuples

print(combo) #print the super tuple

# 6
print("\n-6-")

hero = ("Batman", "Superman", "Aquaman", "Deadpool")
 
for i in range(len(hero)): #for each individual hero
    if hero[i] != "Deadpool": #if the hero isn't deadpool
        print(hero[i]) #print the hero name
    
# 7
print("\n-7-")

friends = ("Monica", "Joey", "Chandler") #make the tuple

print(friends[1]) #print the 2nd thing in the tuple

married = friends[0] + " and " + friends[1] #make the string with the 1st and 2nd things in the tuple
print(married) #print their names

# 8 
print("\n-8-")

friends = ("Monica", "Joey", "Chandler") #make the tuple
howYouDoin = friends[1] #variable of just Joey
slicedJoey = howYouDoin[1:3] #variable of just "oe" as the 2nd and 3rd index
print(slicedJoey) #print "oe"

# 9
print("\n-9-")

def monthDays(tup): #making a function
    for mm in months: #for each month
        if mm == "January" or mm == "March": #if jan or march
            print(mm + " Has 31 days") #print the days
        if mm == "February": #if feb
            print(mm + " Has 28 days") #print the days
        if mm == ("April"): #if april
            print(mm + " Has 30 days") #print the days

months = ("January", "February", "March", "April") #make the tuple

monthDays(months) #call the function

# 10
print("\n-10-")

import random; #importing the random library

def getRands(ceiling): #making the function
    for x in range(1, 10): #run the loop 10 times
        var = random.randint(1, ceiling) #creating a variable for the random number between 0 and the ceiling
        x += 1 #increase x each time to run 10 times
        if var < 3: #if the random number is less than 3
            print(var) #print it
        
getRands(10) #calling the function so it works :)