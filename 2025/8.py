import os
from functools import reduce
import collections

class UnionFind:
    def __init__(self, n):
        self.d = [i for i in range(n)] 

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.d[px] = py
        pass

    def find(self, x):
        if self.d[x] == x:
            return x
        else:
            return self.find(self.d[x])

def f1(f, count):
    coor = []
    for l in f:
        coor.append(l.strip().split(","))
    dist = []
    for i in range(len(coor)):
        for j in range(i + 1, len(coor)):
            x1, y1, z1 = [int(x) for x in coor[i]]
            x2, y2, z2 = [int(x) for x in coor[j]]
            d = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            dist.append((d, i, j))
    dist = sorted(dist)
    #  print(dist)

    uf = UnionFind(len(coor))
    for i in range(count):
        _, p1, p2 = dist[i]
        uf.union(p1, p2)

    for i in range(len(uf.d)):
        uf.d[i] = uf.find(i)

    #  print(uf.d)
    print("====>", reduce(lambda x, y: x * y, sorted(collections.Counter(uf.d).values(), reverse = True)[:3]))


def f2(f):
    coor = []
    for l in f:
        coor.append(l.strip().split(","))
    dist = []
    for i in range(len(coor)):
        for j in range(i + 1, len(coor)):
            x1, y1, z1 = [int(x) for x in coor[i]]
            x2, y2, z2 = [int(x) for x in coor[j]]
            d = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            dist.append((d, i, j))
    dist = sorted(dist)
    #  print(dist)

    unconnect = True
    uf = UnionFind(len(coor))
    for d in dist:
        _, p1, p2 = d
        #  print(d)
        uf.union(p1, p2)

        if unconnect:
            root = p1
            unconnect = False

        if uf.find(p1) == uf.find(root):
            for i in range(len(uf.d)):
                uf.d[i] = uf.find(i)

        #  print(uf.d)

        if len(set(uf.d)) == 1:
            print(p1, p2, int(coor[p1][0]) * int(coor[p2][0]))
            break


    #  print(uf.d)
    #  print("====>", reduce(lambda x, y: x * y, sorted(collections.Counter(uf.d).values(), reverse = True)[:3]))




with open("tmp.txt") as f:
    #  f1(f, 10)
    f2(f)

with open("8.txt") as f:
    #  f1(f, 1000)
    f2(f)
    pass
