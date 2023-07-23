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
    'Method', # class for method metadata
    'methods', # maps string to Methods
    'load_starvote_file', # function
    'Options', # class
    'STAR_Voting', # Method
    'star', # Method (nickname)
    'UsageException', # exception class
    ]

class UsageException(Exception):
    def __init__(self, s=''):
        super().__init__(s)

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

def ranbal(cand=4, ball=3, elec=1, seed=None):
    if ball < 2:
        exit("number of ballots must at minimum 2")
    if cand < 3:
        exit("number of candidates must at minimum 3")
    if elec < 1:
        exit("number of elections must at minimum 1")
    for e in range(elec):
        cand_temp = list(string.ascii_uppercase + string.ascii_lowercase)
        cand_names = cand_temp[0:cand]
        print(cand_names)
        ball_init = [[0] * cand for i in range(ball)]
        for e in ball_init:
            print (e)

ranbal(cand=3, ball=4, elec=1)