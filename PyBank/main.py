import os
import csv

budget_data_1 = os.path.join("Resources", "budget_data_1.csv")
budget_data_2 = os.path.join("Resources", "budget_data_2.csv")
new_budget_data_1 = os.path.join("new_budget_data_2.txt")

with open(budget_data_2, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header= next(csv_reader)
    total_months = sum(1 for row in csv.reader(csvfile))

with open(budget_data_2, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    
    total_revenue = 0
    for row in csv.reader(csvfile):
       total_revenue += int(row[1])

with open(budget_data_2, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header= next(csv_reader)

    previous_month = 0
    revenue_change = []
    month_of_change = []
    for row in csv_reader:
        change_in_revenue = int(row[1]) - int(previous_month)
        revenue_change.append(change_in_revenue)
        month_of_change.append(row[0])
        previous_month = int(row[1])

monthly_revenue = []
sum_of_change = 0

for i in revenue_change:
    sum_of_change = sum_of_change + int(row[1])

average_change = sum_of_change/total_months
month_and_change = dict(zip(month_of_change, revenue_change))
high_change = max(month_and_change.keys(), key=(lambda k: month_and_change[k]))
low_change = min(month_and_change.keys(), key=(lambda k: month_and_change[k]))

import math

print("Financial Analysis")
print("----------------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$" + str(total_revenue))
print("Average Revenue Change: " + "$" + str(math.floor(average_change)))
for key, value in month_and_change.items():
    if key == high_change:
        print("Greatest Increase in Revenue: " + key + " ($" + str(value) + ")")
for key, value in month_and_change.items():
    if key == low_change:
        print("Greatest Decrease in Revenue: " + key + " ($" + str(value) + ")")


with open('new_budget_data_2.txt', 'w') as txtfile:
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("-----------------------------------------------" + "\n")
    txtfile.write("Total Months: " + str(total_months) + "\n")
    txtfile.write("Total Revenue: " + "$" + str(total_revenue) + "\n")
    txtfile.write("Average Revenue Change: " + "$" + str(math.floor(average_change)) + "\n")
    for key, value in month_and_change.items():
        if key == high_change:
            txtfile.write("Greatest Increase in Revenue: " + key + " ($" + str(value) + ")" + "\n")
    for key, value in month_and_change.items():
        if key == low_change:
            txtfile.write("Greatest Decrease in Revenue: " + key + " ($" + str(value) + ")" + "\n")