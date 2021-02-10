import csv
from parse_json import parseJSON
from utilities import dateString

# Opens input file selection window, parses JSON, and outputs as python array of arrays.
# Results are as follows: [[column titles],[data]]
results = parseJSON()

# Creates and writes output file as csv
with open(f"output-{dateString()}.csv", "w", newline="") as c:

    write = csv.writer(c) 
      
    write.writerow(results[0]) 
    write.writerows(results[1])

print(results[0])