# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

#Modules
import os
import csv

#Set Path for File
csvpath = os.path.join("..","budget_data.csv")

#set list
months = [] 
totalrevchange = []

#provide value to variables
totalpl = 0
prevrev = 0 
revchange = 0 
toprevincrease = [0,0]
toprevdecrease = [0,0]


#CSV Module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #skip header
    next(csvreader, None)

    for row in csvreader:
        #add list of "months" into our months list
        months.append(row[0])
        #add up all the profits and loss in row 1/column b
        totalpl = totalpl + int(row[1])

        #max & min change
        revchange = int(row[1]) - int(prevrev)
        if len(totalrevchange) > 0:
            if revchange > int(toprevincrease[1]):
                toprevincrease = [row[0],revchange]
                
            if revchange < int(toprevdecrease[1]):
                toprevdecrease = [row[0],revchange]
                
        
        totalrevchange.append(revchange)
        prevrev = row[1]

    
#print
totalmonths = len(months)
print(totalmonths)
print(totalpl)
print(toprevdecrease)
print(toprevincrease)









