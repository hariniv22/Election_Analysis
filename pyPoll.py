# Add dependencies
import os, csv
# Assign a variable for the file to load and path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable for the file to write the data
file_to_save = os.path.join("Resources", "election_analysis.txt")

# Intialize total_votes to zero
total_votes = 0
# Intializing candidates list
candidate_options = []
# Initializing votes for each candidate
candidate_votes = {}
#Track the winning candidate, vote count, and percentage
winning_candidate = ""  
winning_count = 0
winning_percentage = 0

# Open the election results file and read the data
with open(file_to_load) as election_data:
    # Read the file object with reader function
    file_reader = csv.reader(election_data)
    # Read and print header row
    headers = next(file_reader)
    # Iterate through each row 
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        # If the candidate name is not already present 
        if candidate_name not in candidate_options:
            # Append the name to the candidate list
            candidate_options.append(candidate_name) 
            # Tracking each candidate's vote count
            candidate_votes[candidate_name] = 0

        # Increment each time the candidate's name is seen the row
        candidate_votes[candidate_name] += 1
# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        election_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # print each candidate's name, percentage and total votes to terminal
        print(election_results, end="")
        txt_file.write(election_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary, end="")
    # Save winning candidate's results to text file
    txt_file.write(winning_candidate_summary)


