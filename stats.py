#!/usr/bin/env python3.8
import sys
import argparse
import statistics

parser = argparse.ArgumentParser(description="Math to int file" )
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), help="Input file (default: stdin)", default=sys.stdin)
parser.add_argument("-d", dest='sep', help="Fields separator (default: \"|\")", default="|")
parser.add_argument("-f", dest='field', help="Field pos (default: 0)", default=0)
parser.add_argument("-op", dest='op', help="Operation type (count, mean, cmean, gmean, stdev, var, cvar, median)", default="mean")
args = parser.parse_args()

def ops(name):
    operations = \
        {
            "mean": (1, statistics.mean),
            "count": (1, len),
            "var": (2, statistics.variance),
            "stdev": (2, statistics.stdev),
            "median": (1, statistics.median),
            "gmean": (1, statistics.geometric_mean)
        }
    return operations[name]

data = []

for line in args.infile:
    fields = line.split(args.sep)
    data.append(int(fields[args.field].strip()))
    minsize, op = ops(args.op)
    if len(data) > minsize:
        print(op(data))
