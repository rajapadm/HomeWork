import os
import csv
import math
filepath=os.path.join('raw_data', 'election_data_2.csv')

with open(filepath) as csv1:
    csvreader = csv.DictReader(csv1)
    #ext(csvreader, None)
    total_votes=0
    list_of_candidates = []
    dict_votes = {}
    percentage_votes = {}
    for row in csvreader:
        total_votes += 1
        if row['Candidate'] not in list_of_candidates:
            list_of_candidates.append(row['Candidate'])
        if row['Candidate'] in list_of_candidates:
            if row['Candidate'] in dict_votes:
                dict_votes[row['Candidate']] += 1
            else:
                dict_votes[row['Candidate']] = 1
            
            percentage_votes[row['Candidate']] = float(math.ceil((dict_votes[row['Candidate']]/total_votes)*100))
    winner = max(dict_votes, key=dict_votes.get)
print("\nElection Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
for name in list_of_candidates:
    print(name + ":  " + str(percentage_votes[name]) +"%  " + "("+ str(dict_votes[name])+")")
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")

output=os.path.join('raw_data', 'PyPoll_Results.txt')

with open(output,'w') as text:
    text.write("Election Results")
    text.write("\n------------------------------------")
    text.write(f"\nTotal Votes: {total_votes}")
    text.write("\n------------------------------------\n")
    for name in list_of_candidates:
        text.write(name + ":  " + str(percentage_votes[name]) +"%  " + "("+ str(dict_votes[name])+")\n")
    text.write("------------------------------------------")
    text.write(f"\nWinner: {winner}")
    text.write("\n------------------------------------------")