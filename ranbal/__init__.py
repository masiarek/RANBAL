import builtins
from collections import defaultdict
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

##         * maybe just super-regular HTML, with classes and names to make it easy?
##     * allow displaying in floats
##     * restore printing the preference matrix (it's lurking in 1.x versions)
##

__doc__ = "Create Random Elections and Random Ballots"

__version__ = "0.0.1"

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