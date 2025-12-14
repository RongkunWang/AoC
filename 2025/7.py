import os
import collections

def f1(f):
    mat = []
    q = []
    for x, l in enumerate(f):
        row = []
        l = l[:-1]
        for y, c in enumerate(l):
            row.append(c)
            if c == "S":
                q.append(y)
        mat.append(row)
    print(mat)

    n = 0
    x = 0
    for x in range(len(mat) - 1):
        print(x, q)
        newq = set([])
        for y in q:
            if y < 0 or y >= len(mat[0]): continue
            if mat[x + 1][y] == "^":
                # split down
                n += 1
                newq.add(y-1)
                newq.add(y+1)
            else:
                newq.add(y)
        q = newq
    print(n)

def f2(f):
    mat = []
    q = collections.defaultdict(int)
    for x, l in enumerate(f):
        row = []
        l = l[:-1]
        for y, c in enumerate(l):
            row.append(c)
            if c == "S":
                q[y] = 1
        mat.append(row)
    print(mat)

    x = 0
    out = 0
    for x in range(len(mat) - 1):
        print(x, q)
        newq = collections.defaultdict(int)
        for y, ways in q.items():
            #  if y < 0 or y >= len(mat[0]): 
                #  continue
            if mat[x + 1][y] == "^":
                # split down
                newq[y - 1] += ways
                newq[y + 1] += ways
            else:
                newq[y] += ways
        q = newq
    print(q)
    print(sum(q.values()) + out)




with open("7.txt") as f:
#  with open("tmp.txt") as f:
    #  f1(f)
    f2(f)
