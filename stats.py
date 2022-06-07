#!/usr/bin/env python3
import sys
import argparse
import statistics
from typing import Type

parser = argparse.ArgumentParser(description="Math to int file" )
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), help="Input file (default: stdin)", default=sys.stdin)
parser.add_argument("-d", dest='sep', help="Fields separator (default: \"|\")", default="|")
parser.add_argument("-f", dest='field', help="Field pos (default: 0)", default=0)
parser.add_argument("-op", dest='op', help="Operation to apply (count, sum, mean, cmean, gmean, stdev, var, median)", default="mean")
parser.add_argument("-type", dest='type', help="Data type (int, float)", default="int")
args = parser.parse_args()

def ops(name: str) -> object:
    operations = \
        {
            "mean": (1, statistics.mean),
            "cmean": (2, lambda x: statistics.mean(x) * len(x) / (len(x) - 1)),
            "count": (1, len),
            "var": (2, statistics.variance),
            "stdev": (2, statistics.stdev),
            "median": (1, statistics.median),
            "gmean": (1, statistics.geometric_mean),
            "sum": (1, sum),
        }
    return operations[name]

def converter(t:str) -> Type[int | float]:
    if t == "int":
        return int
    else:
        return float


data = []
minsize, op = ops(args.op)

tp = converter(args.type)

for line in args.infile:
    fields = line.split(args.sep)
    temp = fields[args.field].strip()
    data.append(tp(temp))
    if len(data) > minsize:
        print(op(data))
