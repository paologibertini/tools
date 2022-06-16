#!/usr/bin/env python3
import sys
from os.path import basename
from textwrap import wrap

def main():
    input_data = sys.argv[1:]
    if len(input_data) == 0:
        tmp = input("Insert a hex ip value: ")
        input_data.append(tmp)
    if input_data[0].lower() in ["-h", "--help", "help", "h"]:
        print(f"Usage: {basename(sys.argv[0])} [hex input 1] ... [hex input n]\n",
              "If length [hex input] < 8, input is 0 filled *at end of string*.\n")
        sys.exit()
    for hxip in input_data:
        hxip = ''.join(x for x in hxip if x != ".")
        try:
            if len(hxip) < 8:
                hxip = hxip.ljust(8, "0")
                #print(f"{hxip=}")
            decip = [f"{int(x, 16)}" for x in wrap(hxip, 2)]
            print(".".join(decip))
        except Exception as e:
            print(f"{hxip} is not a valid ip number")

if __name__ == "__main__":
    main()
