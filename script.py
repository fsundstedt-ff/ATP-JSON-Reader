import csv

test_partial = 'sample-2.txt'
test_full = 'baseline-output-01-19-2021.txt'

input_file = open(test_full,'r')

lines = input_file.readlines()

# # CSV block
fields = ['name', 'amount']
csv_data = []

trigger = 'EXPENSES  Dining Out'
name = ''
flag = False

for line in lines:
    if line[0:8].strip() == 'Name:':
        name = line[8:].strip()
    elif line[0:20] == trigger:
        flag = True
    elif line[0] == 'E' and line[0:20] != trigger or line[0] == '-':
        flag = False
    elif line[0] == ' ' and flag:
        csv_entry = [name,float(line[22:28].strip())]
        csv_data.append(csv_entry)

with open('output.csv', 'w', newline='') as c:
      
    # using csv.writer method from CSV package 
    write = csv.writer(c) 
      
    write.writerow(fields) 
    write.writerows(csv_data)
