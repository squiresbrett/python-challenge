import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
csvpath_output = os.path.join("election_analysis.txt")

total_votes = 0
candidates = {}
candidateLS = []

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(csvpath, newline='') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)

    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidateLS:
            candidateLS.append(candidate_name)
            candidates[candidate_name] = 0

        candidates[candidate_name] += 1

    results = []
    for candidate_name in candidates:
        votes = candidates[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        results.append((candidate_name, votes, vote_percentage))
        print((candidate_name, votes, vote_percentage))

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(f"{result[0]}: {result[2]:.3f}% ({result[1]})")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

with open(csvpath_output, 'w') as file:

    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for result in results:
        file.write(f"{result[0]}: {result[2]:.3f}% ({result[1]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winning_candidate}\n")
    file.write("-------------------------\n")
