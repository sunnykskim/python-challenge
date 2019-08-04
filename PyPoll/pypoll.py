# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

#Modules
import os
import csv

#Set Path for File
csvpath = os.path.join("..","election_data.csv")

#variables

winner = []
totalvotes = 0 
khanvotes = 0
correyvotes = 0
livotes = 0
otooleyvotes = 0


#CSV Module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    #skip header
    next(csvreader, None)

    #loop
    for row in csvreader:
        #total vote # counter
        totalvotes += 1

        #tell where candidate_name is 
        candidate_name = row[2]

        #vote count for each candidates
        if candidate_name == "Khan":
            khanvotes += 1
        elif candidate_name == "Correy":
            correyvotes +=1
        elif candidate_name == "Li":
            livotes += 1
        elif candidate_name == "O'Tooley":
            otooleyvotes += 1

    #percentages of vote per candidate
    khanperc = '{:.3f}'.format((int(khanvotes)/int(totalvotes))*100)
    correyperc = '{:.3f}'.format((int(correyvotes)/int(totalvotes))*100)
    liperc = '{:.3f}'.format((int(livotes)/int(totalvotes))*100)
    otooleyperc = '{:.3f}'.format((int(otooleyvotes)/int(totalvotes))*100)
    #figure out winner
    winningvotecount = max(khanvotes,correyvotes,livotes,otooleyvotes)
    if winningvotecount == khanvotes:
        winner.append('Khan')
    elif winningvotecount == correyvotes:
        winner.append('Correy')
    elif winningvotecount == livotes:
        winner.append('Li')
    elif winningvotecount == otooleyvotes:
        winner.append("O'Tooley")

#prints
prt =(
f"Election Results \n"
f"------------------------- \n"
f"Total Votes: {totalvotes} \n"  
f"------------------------- \n"
f"Khan: {khanperc}% ({khanvotes}) \n"
f"Correy: {correyperc}% ({correyvotes}) \n"
f"Li: {liperc}% ({livotes}) \n"
f"O'Tooley: {otooleyperc}% ({otooleyvotes}) \n"
f"------------------------- \n"
f"Winner: {(''.join(winner))} \n"
f"------------------------- \n")
print(prt)

#txt file export

outputtxt = os.path.join('.', 'PyPoll_Analysis.txt')
with open(outputtxt, 'w') as txtfile:
    txtwriter = txtfile.write(prt)

    


            

        

