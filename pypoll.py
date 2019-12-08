import os
import csv

csvpath = os.path.join('..','Onedrive', 'election_data.csv')
print(dir(csv))

candidates = {}
total_votes = 0
with open('election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        if row[2] in candidates.keys():
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1
individual = {}
individual_vote = 0
