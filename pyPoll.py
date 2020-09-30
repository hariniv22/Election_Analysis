# Add dependencies
import os, csv
# Assign a variable for the file to load and path
file_to_load = 'Module3/Election_Analysis/Resources/election_results.csv'
# Assign a variable for the file to write the data
file_to_save = 'Module3/Election_Analysis/analysis/election_analysis.txt'
# Open the election results file and read the data
with open(file_to_load) as election_data:
    # Read the file object with reader function
    file_reader = csv.reader(election_data)
    # Read and print header row
    headers = next(file_reader)
    print(headers)
    # Iterate through each row 
    for row in file_reader:
        print(row)
