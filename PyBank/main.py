###Import libraries
import os
import csv

###Create file path
file_path = os.path.join('Resources', 'budget_data.csv')

###Open the file and quick view the data
with open(file_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    # # print(list(csvreader))

    # csv_header = next(csvreader)
    # # print(f"CSV Header: {csv_header}")

###Skip the header after view
    next(csvreader, None)

###Lists for calculations
    totalmonths = []
    totalamount = []
    changeamount = []

    for row in csvreader:
        totalmonths.append(row[0])
    # print(len(totalmonths))
        totalamount.append(int(row[1]))
    # print(totalamount)
    for i in range(len(totalamount)-1):
        changeamount.append(totalamount[i+1]-totalamount[i])
    # print(changeamount)

###Print Info
    print ("Financial Analysis")
    print ("-------------------------------")
    print (f"Total Months: ", len(totalmonths))
    print (f"Total: ${sum(totalamount)}")
    print (f"Average Change: ${round(sum(changeamount)/len(changeamount),2)}")
    print ("Greatest Increase in Profits: ", f"${max(changeamount)}")
    print ("Greatest Decrease in Profits: ", f"${min(changeamount)}")

###Export
f = open('new.txt', 'a')

f.write("Financial Analysis")
f.write("-------------------------------")
f.write(f"Total Months: {len(totalmonths)}")
f.write(f"Total: ${sum(totalamount)}")
f.write(f"Average Change: ${round(sum(changeamount)/len(changeamount),2)}")
f.write(f"Greatest Increase in Profits: ${max(changeamount)}")
f.write(f"Greatest Decrease in Profits: ${min(changeamount)}")

f.close()
