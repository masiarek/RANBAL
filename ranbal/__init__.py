import builtins
from collections import defaultdict
import collections  # ?
from contextlib import contextmanager
import csv
from fractions import Fraction
import enum
import itertools
from math import floor, log10
import os
import pathlib
import random
import re
import sys
import types
import string

__doc__ = "Create Random Elections and Random Ballots"

__version__ = "0.0.2"

__all__ = [
    'UsageException', # exception class
    ]

class UsageException(Exception):
    def __init__(self, s=''):
        super().__init__(s)
_DEFAULT_SEATS = 1
_DEFAULT_MAXIMUM_SCORE = 5
def main_with_usage(argv, print=builtins.print):
    try:
        main(argv, print=print)
    except UsageException as e:
        s = str(e)
        if s:
            print(s)
            print()
        print(f'''
usage: ranbal.py [options] <ballots_file>

Create Random Elections and Random Ballots
Options:
    -s|--seats <seats>

        Specifies number of seats, default {_DEFAULT_SEATS}.
        Required when method is not STAR.

    -x|--maximum-score <maximum_score>

        Specifies the maximum score per vote, default {_DEFAULT_MAXIMUM_SCORE}.

'''.strip() + "\n")

        return -1

def ranbal(cand=4, ball=3, elec=1, seed=None, sparsity='medium', max=_DEFAULT_MAXIMUM_SCORE):
    if ball < 2:
        exit("number of ballots must minimum 2")
    if cand < 3:
        exit("number of candidates must at minimum 3")
    if elec < 1:
        exit("number of elections must at minimum 1")
    random.seed(seed)
    for e in range(elec):
        cand_temp = list(string.ascii_uppercase + string.ascii_lowercase)
        cand_names = cand_temp[0:cand]
        candidates = ", ".join(cand_names)
        print(candidates)
        ball_init = [[0] * cand for i in range(ball)]
        fav_index_1 = random.randint(0, cand - 1) # assume some candidates are preferred
        fav_index_2 = random.randint(0,cand - 1)  # by majority of voters
        print(fav_index_1, fav_index_2)
        for e in ball_init:
            if sparsity == 'high': # each row should have at least one/two scores
                if cand <= 4:
                    index1 = random.randint(0,cand - 1)
                    e[index1] = random.randint(4, max)
                    if (random.randint(0, 99) % 3) == 0:
                        e[fav_index_1] = random.randint(2, max)
                else:
                    e[fav_index_1] = random.randint(4, max)
                    index1 = random.randint(0, cand - 1)
                    e[index1] = random.randint(1, max)
                    index2 = random.randint(0, cand - 1)
                    e[index2] = random.randint(5, max)
                    if (random.randint(0, 99)) % 4 == 0:
                        e[fav_index_1] = random.randint(2, max)
                        e[fav_index_2] = random.randint(3, max)
            print(e)

ranbal(cand=4, ball=22, elec=1, sparsity='high')