s = """\
   G,B,P,R,O
18:5,1,2,4,3
12:1,5,2,3,4
10:1,4,5,2,3
9: 1,2,4,5,3
4: 1,4,2,3,5
2: 1,2,4,3,5
"""

# Split the input string into lines
lines = s.strip().split("\n")

# Extract the candidate names
candidates = lines[0].split(",")

# Initialize an empty dictionary to store the results
results = {}

# Parse the vote counts and store them in the dictionary
for line in lines[1:]:
    parts = line.split(":")
    count = int(parts[0])
    votes = list(map(int, parts[1].split(",")))
    results[count] = votes

# Create the formatted output string
t = ""
for count, votes in sorted(results.items(), reverse=True):
    t += f"{count} ballots:\n"
    for i, candidate in enumerate(candidates):
        t += f"{candidate} = {votes[i]}\n"
    t += "\n"

# Print the formatted output
print(t)


"""
18 ballots:
G = 5
B = 1
P = 2
R = 4

12 ballots:
G = 1
B = 5
P = 2
R = 3

10 ballots:
G = 1
B = 4
P = 5
R = 2

9 ballots:
G = 1
B = 2
P = 4
R = 5

4 ballots:
G = 1
B = 4
P = 2
R = 3

2 ballots:
G = 1
B = 2
P = 4
R = 3

"""
