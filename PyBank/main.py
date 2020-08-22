import os
import csv

file_path = os.path.join('Resources', 'budget_data.csv')

with open(file_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    # print(list(csvreader))

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)