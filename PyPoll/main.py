###Import libraries
import os
import csv

###Create file path
file_path = os.path.join('Resources', 'election_data.csv')

###Open the file and quick view the data
with open(file_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    # # print(list(csvreader))

    # csv_header = next(csvreader)
    # # print(f"CSV Header: {csv_header}")

# ###Skip the header after view
    next(csvreader, None)

# ###Lists for calculations
    totalvotes = []
    actualcandidates = []


    for row in csvreader:
        totalvotes.append(row[0])
    # print(len(totalvotes))
        actualcandidates.append(row[2])
    # print(actualcandidates)
        set_index(actualcandidates)
