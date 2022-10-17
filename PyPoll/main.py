#Importing dependencies
import os
import csv

# Set path for files
cvspath = os.path.join('Resources', "election_data.csv")
output_path = os.path.join('analysis',"Election_Results.txt")

#Lists to store data

total_votes=0
candidates_all=[]
can_votes=[]

with open(cvspath) as csvfile:
    csvreader = csv.reader(csvfile)
    
    csvheader=next(csvreader)

    for row in csvreader:
        total_votes+=1
        can_list = (row[2])
        if can_list in candidates_all:
            candidateindex = candidates_all.index(can_list)
            can_votes[candidateindex] = can_votes[candidateindex] + 1
        else:
            candidates_all.append(can_list)
            can_votes.append(1)
        
percent = []
max_votes = can_votes[0]
max_index = 0

for x in range(len(candidates_all)):
    vote_perc = round(can_votes[x]/total_votes*100, 3)
    percent.append(vote_perc)
    if can_votes[x] > max_votes:
        max_votes = can_votes[x]
        max_index = x
electionwinner = candidates_all[max_index]

#Printing
print ('\n')
print("Election Results")
print("-"*25)
print(f"Total Votes: {total_votes}")
print("-"*25)
for x in range(len(candidates_all)):
    print(f'{candidates_all[x]} : {percent[x]:.3f}% ({can_votes[x]})')

#Printing of data analysis results within Terminal
print('Election Results')
print('-'*25)
print(f'Total Votes: {total_votes}')
print('-'*25)
for x in range(len(candidates_all)):
    print(f'{candidates_all[x]} : {percent[x]:.3f}% ({can_votes[x]})')
print('-'*25)
print(f'Winner: {electionwinner}')
print('-'*25)
#Printing of data analysis results to text file
with open(output_path, "w+") as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write('-------------------------\n')
    for x in range(len(candidates_all)):
        txtfile.write(f'{candidates_all[x]} : {percent[x]:.3f}% ({can_votes[x]})\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Winner: {electionwinner}\n')
    txtfile.write('-------------------------\n')
