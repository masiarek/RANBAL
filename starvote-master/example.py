import starvote

ballots = [
    {"Cab": 4, "B": 3, "C": 5},
    {"Cab": 3, "B": 4, "C": 2},
    {"Cab": 3, "B": 4, "C": 1},
    {"Cab": 2, "B": 1, "C": 1},
]

winners = starvote.election(starvote.star, ballots, verbosity=1)
