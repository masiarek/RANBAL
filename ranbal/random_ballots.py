import random
import string

DEFAULT_SEATS = 1
MAX_SCORE = 5
candidates = 3
ballots = 5
elections = 3


def ranbal(cand=candidates, ball=ballots, seed=None, max=MAX_SCORE):
    if ball < 2:
        exit("number of ballots must minimum 2")
    if cand < 3:
        exit("number of candidates must at minimum 3")
    random.seed(seed)

    cand_temp = list(string.ascii_uppercase + string.ascii_lowercase)
    cand_names = cand_temp[0:cand]
    candidates = ", ".join(cand_names)

    ball_init = [[0] * cand for i in range(ball)]
    for e in ball_init:
        index1 = random.randint(0, cand - 1)
        e[index1] = random.randint(1, max)
    return (candidates, ball_init)


candidates, ballots = ranbal()
print(candidates)
for e in ballots:
    print(e)


# how to feed the 'candidates' and random 'ballots' to
# starvote-master/starvote/__init__.py
# step one - reformat from
"""
Cab, B, C, D
[5,2, 4, 1]
"""
# to expected format
"""
Cab = 5
B = 2
C = 4
D = 1
"""
# step 2
# find the winner using starvote-master/starvote/__init__.py
