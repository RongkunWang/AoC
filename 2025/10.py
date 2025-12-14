import os
import math
import numpy as np
import collections
from z3 import *
#  import matplotlib as mpl
#  import matplotlib.pyplot as plt
#  from matplotlib.patches import Polygon

def solve1(l):
    goal, l = l[1:-1].split("]")
    goal_int = 0
    for i, c in enumerate(goal):
        if c == "#":
            goal_int += 2 ** i

    #  print(goal_int)
    l, energy = l.split("{")
    #  print(energy)

    buttons =  [[int(i) for i in w[1:-1].split(',')] for w in l.split()] 
    #  print("buttons", buttons)
    nbuttons = len(buttons)

    maxlight = 0
    for button in buttons:
        for light in button:
            maxlight = max(maxlight, light)
    state = [0] * maxlight

    # is the starting query
    q = [[i] for i in range(len(buttons))]
    i = 0
    while i < len(q):
        all_pressed_buttons = q[i]

        state = 0
        for button in all_pressed_buttons:
            for light in buttons[button]:
                state ^= (0b1 << light)
        #  print(all_pressed_buttons, state)

        if state == goal_int:
            return len(all_pressed_buttons)

        # fill
        for next_button in range(all_pressed_buttons[-1] + 1, nbuttons):
            q.append(  q[i] + [next_button] )
        i += 1

    return 0

def solve2(l):
    _, l = l[1:-1].split("]")

    #  print(goal_int)
    l, energy = l.split("{")
    energy = [int(i) for i in energy.split(",")]
    buttons =  [[int(i) for i in w[1:-1].split(',')] for w in l.split()] 
    #  print("buttons", buttons)
    nbuttons = len(buttons)
    print("start a new line")
    print("buttons", buttons)
    print("energy",  energy)
    print()

    mat = [[0] * nbuttons for i in range(len(energy))]
    for j, but in enumerate(buttons):
        for i in but:
            mat[i][j] = 1
    print(mat)

    X = IntVector('x', len(buttons))

    s = Optimize()
    for k in range(len(buttons)):
        s.add([x >= 0 for x in X])

    for i in range(len(energy)):
        s.add(Sum([X[k] * mat[i][k] for k in range(len(buttons))]) == energy[i])
    s.minimize(Sum(X))

    if s.check() == sat:
        model = s.model()
        return sum(model[k].as_long() for k in model)
    else:
        print("No solution found.")



    upper_lim = []
    for but in buttons:
        upper_lim.append( min([energy[light] for light in but]) )
        pass
    print(upper_lim)


    def dfs(state, npress, cur_min, start_button):
        if npress >= cur_min[0]:
            return False

        all_equal = True
        #  print(state, npress, cur_min)
        for i, j in zip(state, energy):
            if i > j: return False
            if i < j: all_equal = False
        if all_equal: 
            cur_min[0] = npress
            print(npress)
            return False

        #  for ibut, npress in enumerate(press):
                #  if state[level] > energy[level]:
                    #  early_stop = True
                    #  break
            #  if early_stop:
                #  break
        #  if early_stop:
            #  return 0

        for ibut in range(start_button, nbuttons):
            for add_press in range(upper_lim[ibut] + 1):
                for level in buttons[ibut]:
                    state[level] += add_press
                res = dfs(state, npress + add_press, cur_min, start_button + 1)
                for level in buttons[ibut]:
                    state[level] -= add_press
                if not res: break

        return True

    state = [0] * len(energy)
    cur_min = [math.inf]
    dfs(state, 0, cur_min, 0)
    print(cur_min)
    return cur_min[0]

def f1(f):
    s = 0
    for l in f:
        s += solve1(l.strip())
    print(s)
def f2(f):
    s = 0
    for l in f:
        s += solve2(l.strip())
    print(s)

with open("tmp.txt") as f:
    f2(f)
    pass

print()

with open("10.txt") as f:
    f2(f)
    pass
