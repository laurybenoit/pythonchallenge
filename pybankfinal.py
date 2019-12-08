import os 
import csv

# import math
print(dir(csv))

csvpath = os.path.join('..','Onedrive', 'budget_data.csv')

#Variable declaration
number_of_months = 0
change_months = []
net_changes_months = []
increase = [""]
decrease = []
net_total_amount = 0

with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 

    next(csv_reader)
    net_total_amount = net_total_amount + int(next[1])
    last_net = int(next[1])

    for row in csv_reader:
        number_of_months = number_of_months + 1
        net_total_amount = net_total_amount + int(row[1])
        net_change = int(row[1]) - last_net
        last_net = int(row[1])
        net_changes_months = net_changes_months +[net_change]
        change_months = change_months + [row[0]]
        if net_changes_months > increase[1]:
            increase[0] = row[0]
            increase[1] = net_changes_months
        if net_changes_months < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = net_changes_months
average = sum(net_changes_months)/len(net_changes_months)

txt_output = (f"\nFinancial Analysis\n"
              f"--------------------\n)"
              f"Total Months:{number_of_months}\n"
              f"Averages Change: ${net_change}\n"
              f"Greatest Increase in profit: {increase[0]} (${increase[1]})\n"
              f"Greatest Decrease in profit: {decrease[0]}(${decrease[1]})\n)
print(txt_output)

with open()
