'''

Python Lab #2

Eric Lloyd

'''

# 1
print("\n-1-")
#variable for the int 31
dayNum = 31
#printing the sentence
#turning DayNum into a string to concatenate
print("August has " + str(dayNum) + " days.")

# 2
print("\n-2-")
#creating the month variables
sep = "September"
apr = "April"
jun = "June"
nov = "November"
#saving the variable with the concatenated variables
statement = "Thirty days have " + sep + ", " + apr + ", " + jun + ", and " + nov
#printing the statement
print(statement)

# 3
print("\n-3-")
#
oct = "October"
#if oct says October
if oct == "October":
    print("31 days") #print "31 days"
else: #if not, 
    print("30 days") #print "30 days"
# using if/else instead of if/if or if/elif 
# because I want it to print "30 days" if the if is FALSE
    
# 4
print("\n-4-")
#creating int variable
seventy = 70
if seventy % 5 == 0 and seventy % 10 == 0: #if 70 is divisible by these
    print("Number is divisible by 5 and 10.") #print this
else: #if not
    print("Number is NOT divisible by 5 and 10.") #print this
print(" ") #second if statement since we want to test two separate things
if seventy % 7 == 0 or seventy % 2 == 0: #if 70 is divisble by 2 or 7
    print("Number is divisible by 7 or 2.") # print this
else: #if not
    print("Number is NOT divisible by 7 or 2.") #print this
    
# 5
print("\n-5-")
#while x is 1 to before 11
for x in range(1, 11):
    print(x) # print the number
    
# 6
print("\n-6-")
for x in range(6, 21, 3): #if x is between 6 and before 21
    print(x) #print every 3rd number
    
# 7
print("\n-7-")
for set in range(1,6): #when the set is between 1 and 5
    print("Set: " + str(set)) #print the set number
    for num in range (1, 6): #if the student num is between 1 and 5
        if set % 2 == 0: #and if the set is divisble by 2
            print("Student " + str(num)) #print the student number

# 8
print("\n-8-")
x = 0 #x starts at 0
while x < 10: #while x is less than 10
     x += 1 #increase it by one every loop
     if x % 3 == 0: #if x is divisible by 3
         print(x) #print x

  
# 9
print("\n-9-") 
#creating the function doCalc and giving it 3 parameters
def doCalc(num1, num2, num3):
    print((num1 + num2) * num3) #printing the function
    
doCalc(10, 12, 40) #calling it once with these
#this will print the equation using the numbers given

# 10
print("\n-10-")
def creditsPerQuarter(student, numCreds, numCourses): #creating the function
    total = numCreds * numCourses #creating the variable for total credits per quarter
    print(student + " is taking " + str(numCourses) + " courses and each course is " +  str(numCreds) + " credits for a total of " + str(total))
    #making the sentence
    print(" ") #adding a space between returns
creditsPerQuarter("Wade", 3, 4) #printing the 3 students' credit loads
creditsPerQuarter("Bob", 3, 5)    
creditsPerQuarter("Bob", 5, 3)    