#!/usr/bin/env python3

from . import main_with_usage
import sys

sys.exit(main_with_usage(sys.argv[1:]))
# sys.exit(main_with_usage(['test_elections/temp/x2.csv']))
