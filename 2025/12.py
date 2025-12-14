import os
import math
import numpy as np
#  import matplotlib as mpl
#  import matplotlib.pyplot as plt
#  from matplotlib.patches import Polygon

def solve1(l, ntile_presents, presents):
    print(l)
    size, nums = l.split(":")

    l, w = [int(i) for i in size.split("x")]
    area = l*w

    nums = [int(i) for i in nums.strip().split()]
    print(nums)
    required_area = sum([i * j for i, j in zip(ntile_presents, nums)])
    if required_area > area: return 0
    else: return 1

def f1(f):
    iPresent = 0
    i = 0
    presents = []
    present = ["", "", ""]
    ntile_presents = []
    ntile = 0
    s = 0
    for i, l in enumerate(f):
        l = l.strip()
        if iPresent == 6:
            if not l: continue
            s += solve1(l, ntile_presents, presents)

        elif i % 5 == 0: 
            continue
        elif i % 5 == 4:
            presents.append(present)
            ntile_presents.append(ntile)
            present = ["", "", ""]
            ntile = 0
            iPresent += 1
        else:
            present[i % 5 - 1] = l
            ntile += l.count("#")
    print(presents, ntile_presents)
    print(s)


with open("tmp.txt") as f:
    f1(f)
    pass

print()

with open("12.txt") as f:
    f1(f)
    pass
