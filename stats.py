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
            "mean": statistics.mean,
            "count": len,
            "var": statistics.variance,
            "stdev": statistics.stdev,
            "median": statistics.median,
            "gmean": statistics.geometric_mean
        }

data = []

for line in args.infile:
    fields = line.split(args.sep)
    data.append(int(fields[args.field].strip()))
    print(ops(args.op)(data))
