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

#CSV Module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    #set list
    months = []
    MoMdelta = [] 

    #provide value to variables
    totalpl = 0
    pastrev = 0
    highestinc = 0
    highestdec = 999999999
    totalmomdelta = 0
    
    #skip header
    next(csvreader, None)

    for row in csvreader:
        #add list of "months" into our months list
        months.append(row[0])
        #add up all the profits and loss in row 1/column b
        totalpl = totalpl + int(row[1])
        #create a list of MoM change
        revenuechange = int(row[1]) - pastrev
        pastrev = int(row[1])
        MoMdelta.append(revenuechange)
        #dont forget to calculate average avg of MoMdelta outside 
        #greatestincrease
        if (revenuechange > highestinc):
            highestincdate = row[0]
            highestinc = revenuechange
        #greatestdecrease
        if (revenuechange < highestdec):
            highestdecdate = row [0]
            highestdec = revenuechange
    #calculate average of MoMdelta        
    del MoMdelta[0]
    avgmomdelta = sum(MoMdelta)/(len(months) - 1)
    
#print
totalmonths = len(months)
print(totalmonths)
print(totalpl)
print(avgmomdelta)
print(highestinc)
print(highestincdate)
print(highestdec)
print(highestdecdate)
print(MoMdelta)







