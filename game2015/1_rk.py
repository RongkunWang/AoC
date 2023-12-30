#!/usr/bin/env python3
import sys

with open( sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        up = line.strip().count("(")
        down = line.strip().count(")")
        print(up - down)

    #  print(line)
    s = 0
    for i, c in enumerate(line):
        if c == "(": s+= 1
        else: s-= 1

        if s < 0:
            print(i+1)
            break
