#!/usr/bin/env python
import sys
import collections
import math

def parse():
    return int(sys.argv[1])

    n = 0
    with open(sys.argv[1], 'r') as infile:
        for line in infile:
            n = int(line)
            break
    return n

def sol1(n):
    selves = n // 10
    houses = [0] * (selves + 1)
    for elf in range(1, selves+1):
        for house in range(elf, selves+1, elf):
            houses[house] += elf*10
            pass
        pass

    for i in range(1, selves):
        if houses[i] >= n:
            return i

def sol2(n):
    selves = n // 11
    houses = [0] * (selves + 1)
    for elf in range(1, selves+1):
        nhouse = 0
        for house in range(elf, selves+1, elf):
            houses[house] += elf * 11
            nhouse += 1
            if nhouse == 50:
                break
            pass
        pass

    for i in range(1, selves):
        if houses[i] >= n:
            return i

def main():
    n = parse()
    #  print(sol1(n))
    print(sol2(n))
    pass

main()
