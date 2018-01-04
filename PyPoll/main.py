import os
import csv

election_data_1 = os.path.join("Resources PyPoll", "election_data_1.csv")
election_data_2 = os.path.join("Resources PyPoll", "election_data_2.csv")
new_election_data_1 = os.path.join("new_election_data_1.txt")

vote_list = []
cand_dict = {}
cand_names = []
with open(election_data_2, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    total_votes = sum(1 for row in csv.reader(csvfile))


with open(election_data_2, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    for row in csv_reader:
        if row[2] not in cand_names:
            cand_names.append(row[2])
            cand_dict[row[2]] = 0
        cand_dict[row[2]] = cand_dict[row[2]] + 1

winner = max(cand_dict.keys(), key=(lambda k: cand_dict[k]))

import math

print(" ")
print("Election Results")
print("-----------------------------------------------")
print("Total Votes:", total_votes)
print("-----------------------------------------------")
for key in cand_dict:
    print(key, ":", str(math.floor(100 * (cand_dict[key]/total_votes)))+ '.0' + '%',"(" + str(cand_dict[key]) + ")")
print("-----------------------------------------------")
print("Winner:", winner)
print("-----------------------------------------------")


with open('new_election_data_2.txt', 'w') as txtfile:
    txtfile.write("Election Results" + "\n")
    txtfile.write("-----------------------------------------------" + "\n")
    txtfile.write("Total Votes:" + str(total_votes) + "\n")
    txtfile.write("-----------------------------------------------" + "\n")
    for key in cand_dict:
        txtfile.write(key + ":" + str(math.floor(100 * (cand_dict[key]/total_votes)))+ '.0' + '%' + "(" + str(cand_dict[key]) + ")" + "\n")
    txtfile.write("-----------------------------------------------" + "\n")
    txtfile.write("Winner:" + winner + "\n")