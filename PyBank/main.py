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

#define for variable for clean print block    
totalmonths = len(months)
#rounding avgmomdelta int
avgmomdelta = round(avgmomdelta,2)

#prints
prt = (
f"Financial Analysis \n"
f"------------------------- \n"
f"Total Months: {totalmonths} \n"
f"Total: ${totalpl} \n"
f"Average Change: (${avgmomdelta}) \n"
f"Greatest Incrase in Profits: {highestincdate} (${highestinc}) \n"
f"Greatest Decrease in Profits: {highestdecdate} (${highestdec}) \n")
print(prt)


#txt file export

outputtxt = os.path.join('.', 'PyBank_Analysis.txt')
with open(outputtxt, 'w') as txtfile:
    txtwriter = txtfile.write(prt)






