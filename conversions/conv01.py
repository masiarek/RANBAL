from collections import defaultdict

# Example ballots text
ballots_text = """
1000 Z>P>Q>R>S>T>U>V>W>X>Y>A
512  P>Q>R>S>T>U>V>W>X>Y>A>Z
256  Q>R>S>T>U>V>W>X>Y>A>P>Z
128  R>S>T>U>V>W>X>Y>A>P>Z>Q
64   S>T>U>V>W>X>Y>A>P>Z>Q>R
32   T>U>V>W>X>Y>A>P>Z>Q>R>S
16   U>V>W>X>Y>A>P>Z>Q>R>S>T
8    V>W>X>Y>A>P>Z>Q>R>S>T>U
4    W>X>Y>A>P>Z>Q>R>S>T>U>V
2    X>Y>A>P>Z>Q>R>S>T>U>V>W
1    Y>A>P>Z>Q>R>S>T>U>V>W>X
2    A>P>Z>Q>R>S>T>U>V>W>X>Y
"""

# Parse the ballots text
source_rankings = []
for line in ballots_text.strip().split("\n"):
    parts = line.split()
    count = int(parts[0])
    ranking = parts[1]
    source_rankings.append((ranking, count))

# Extract candidates and find the maximum score
candidates = set()
for ranking, _ in source_rankings:
    candidates.update(ranking.split(">"))
max_score = len(candidates)

# Convert source rankings to target scoring format
target_scores = defaultdict(dict)
for ranking, count in source_rankings:
    candidates = ranking.split(">")
    for i, candidate in enumerate(candidates):
        target_scores[count][candidate] = max_score - i

# Print the results
for count, scores in target_scores.items():
    print(f"{count} ballots:")
    for candidate, score in scores.items():
        print(f"{candidate} = {score}")
