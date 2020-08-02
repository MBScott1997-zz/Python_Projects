'''

Python Lab #5

Michael Scott

'''

import csv

# 1

print("\n-1-")

with open("DataSamples/DontQuit.txt", "r") as reader: #opening the .txt and read
    print(reader.readline()) #printing first line

# 2

print("\n-2-")

with open("DataSamples/DontQuit.txt", "r") as reader: #opening the .txt and read
    line = reader.readline()
    
    while line != '':
        print(line, end='')
        line = reader.readline()
# 3

print("\n\n-3-")
with open("DataSamples/DontQuit.txt", "r") as reader:
    line = reader.readline()
    for line in reader:
        if "Life" in line:
            print(line, end=' ')
            
# 4 
            
print("\n-4-")

list = ["Please excuse my dear Aunt Sally\n", "Roy G. Biv\n"]

with open("DataSamples/famousSayings.txt", "w+") as reader:
    reader.write("My very excited mother just served us nine pies.\n")
# ^^^ writing to a new file
with open("DataSamples/famousSayings.txt", "a+") as reader:
    reader.writelines(list)
# ^^^ appending the list to the .txt
with open("DataSamples/famousSayings.txt", "r") as reader:
    for i in reader:
        print(i)
# ^^^ printing
        
# 5
        
print("\n-5-")

with open("DataSamples/famousSayings.txt", "a+") as reader:
    reader.write("Will a jolly man make a jolly visitor?")
# ^^^ appending to the .txt
with open("DataSamples/famousSayings.txt", "r") as reader:
    for i in reader:
        print(i)
# ^^^ printing
        
# 6
print("\n-6-")

# 7
print("\n-7-")

with open("DataSamples/DogWeights.csv", "w+") as csv_file: #opening the dogweights to write to it
    fieldnames = ["Name", "Weight"] #naming the columns
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames) #writing to the .csv file
    
    writer.writeheader() #no header
    writer.writerow({"Name": "Spot", "Weight":53}) #making the rows
    writer.writerow({"Name": "Sadie", "Weight":22})
    writer.writerow({"Name": "Sammie", "Weight":24})
    writer.writerow({"Name": "Jasper", "Weight":45})
    
with open("DataSamples/DogWeights.csv", "r+") as csv_file: #reopening it to read it
    csv_reader = csv.DictReader(csv_file) #reading it
    
    for i in csv_reader: #for each cell
        for k, v in i.items(): #for each name and weight
            print(k + ': ' + v) #print them