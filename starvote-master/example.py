import starvote

ballots = [
    {'A': 4, 'B': 3, 'C': 5},
    {'A': 3, 'B': 4, 'C': 2},
    {'A': 3, 'B': 4, 'C': 1},
    {'A': 2, 'B': 1, 'C': 1},
]

winners = starvote.election(starvote.star, ballots, verbosity=1)