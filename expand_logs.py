#!/bin/env python3
import csv
import argparse
import sys


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help="Input file", nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument("--input_line_number", "-iln", help="Show input line number", dest="input_line_number",
                        action="store_true")
    parser.add_argument("--output_line_number", "-oln", help="Show output line number", dest="output_line_number",
                        action="store_true")
    #parser.add_argument("-grep", nargs="+", help="Filter input file for list of values")
    parser.add_argument("--description_file", "-d", help="Header file", dest="header", action="store")
    parser.add_argument("-sep", "--separator", dest="separator", help="Fields separator", default=",")
    return parser.parse_args()


def header_file(filename):
    try:
        with open(filename, "r") as header_file:
            header = header_file.readline()
            return header.split(",")
    except TypeError as e:
        return None
    except FileNotFoundError as e:
        print("Header file not found")
        return None

def output_line():
    i = 0
    while True:
        i += 1
        yield i


def log_parser(parse, header):
    logfile = parse.infile
    input_line_number = 0
    gen_output_line_number = output_line()
    for raw_row in logfile:
        row = raw_row.rstrip()
        fields = row.split(parse.separator)
        input_line_number += 1
        if not header:
            header = fields
            continue
        outfields = [f"{key}={value}" for key, value in zip(header, fields)]
        output_line_number = next(gen_output_line_number)
        output = f"{input_line_number}:" if parse.input_line_number else ""
        output += f"{output_line_number}:" if parse.output_line_number else ""
        output += f"{', '.join(outfields)}"
        print(output)


def main():
    parser = parseArgs()
    #print(parser)
    header = header_file(parser.header)
    log_parser(parser, header)


if __name__ == '__main__':
    main()

