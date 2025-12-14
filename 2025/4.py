import os

def count(x, y, mat):
    m = len(mat)
    n = len(mat[0])
    c = 0
    for i in range(x - 1, x + 2):
        if i < 0 or i >= m: continue
        for j in range(y - 1, y + 2):
            if j < 0 or j >= n: continue
            if i == x and j == y: continue
            if mat[i][j] == "@": c += 1
    return c

def f1(f):
    mat = []
    for l in f:
        mat.append( l.strip() )
    m = len(mat)
    n = len(mat[0])
    print(mat)
    paper = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == "@" and count(i, j, mat) < 4:
                print(i, j)
                paper += 1
    print(paper)

def flatten(mat):
    return [c for row in mat for c in row]

def f2(f):
    mat = []
    for l in f:
        mat.append( [c for c in l.strip()] )
    m = len(mat)
    n = len(mat[0])

    paper = 0
    while True:
        print(mat)
        prev_mat = flatten(mat)
        for i in range(m):
            for j in range(n):
                if mat[i][j] == "@" and count(i, j, mat) < 4:
                    print(i, j)
                    paper += 1
                    mat[i][j] = '.'
        if flatten(mat) == prev_mat:
            break
    print(paper)
    pass

def main(f):
    #  f1(f)
    f2(f)


with open("4.txt") as f:
#  with open("tmp.txt") as f:
    main(f)
