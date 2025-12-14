import os
import numpy as np
import collections
#  import matplotlib as mpl
#  import matplotlib.pyplot as plt
#  from matplotlib.patches import Polygon

def f1(f):
    mat = []
    for l in f:
        x, y = [int(i) for i in l.strip().split(',') ]
        mat.append((x, y))

    n = 0
    for i in range(len(mat)):
        for j in range(i+1, len(mat)):
            x1, x2 = min(mat[i][0], mat[j][0]), max(mat[i][0], mat[j][0])
            y1, y2 = min(mat[i][1], mat[j][1]), max(mat[i][1], mat[j][1])
            s = (x2 - x1 + 1) * (y2 - y1 + 1)
            n = max(s, n)
    print(n)

def f2(f, sx, sy):
    # mat for line scan
    red = []
    maxm = 0
    for l in f:
        x, y = [int(i) for i in l.strip().split(',') ]
        red.append([x, y])
        maxm = max(x + 1, y + 1, maxm)

    #  fig, ax = plt.subplots()
    #  ax.set_xlim(0, maxm)
    #  ax.set_ylim(0, maxm)
    #  #  print(np.random.rand(50, 2))
    #  y = np.array([np.array([x for x in xi], dtype = float) for xi in red])
    #  #  print(y)
    #  polygon = Polygon(y, closed=True)
    #  ax.add_patch(polygon)
    #  plt.show()

    #  print(red)
    #  print(maxm)
    #  matx = [[] for _ in range(maxm)]
    #  maty = [[] for _ in range(maxm)]
    #  mat = [[] for _ in range(maxm)]
    xedge = []
    yedge = []

    # fill the boundary
    px, py = -1, -1
    for x, y in red + [red[0]]:
        if px != -1:
            if px == x:
                xedge.append((x, min(py, y), max(py, y)))
                #  matx[x].append([min(py, y), max(py, y)])
                #  mat[x].append([min(py, y), max(py, y)])
            else:
                yedge.append((y, min(px, x), max(px, x)))
                #  maty[y].append([min(px, x), max(px, x)])
                #  for xi in range(min(px, x), max(px, x) + 1):
                    #  mat[xi].append([y, y])
        px, py = x, y

    #  print("\nborder x", matx)
    #  print("border y", maty)
    
    #  mat = [sorted(l) for l in mat]
    #  # cleanup mat
    #  for x in range(maxm):
        #  if len(mat[x]) == 0: continue
        #  nl = [ [mat[x][0][0], mat[x][0][1]] ]
        #  for i in range(1, len(mat[x])):
            #  if mat[x][i][0] == nl[-1][1]:
                #  if nl[-1][1] == nl[-1][0]:
                    #  nl[-1][1] = mat[x][i][1]
            #  else:
                #  nl.append([mat[x][i][0], mat[x][i][1]])
        #  mat[x] = nl

    #  # process
    #  for x in range(maxm):
        #  if len(mat[x]) == 0: continue
        #  inside = True
        #  if len(mat[x]) == 1: continue

        #  nl = []
        #  for i in range(1, len(mat[x])):
            #  if inside:
                #  nl.append([mat[x][i-1][0], mat[x][i][1]])
            #  inside = not inside
        #  mat[x] = nl

    #  print(mat)

    #  for x in range(maxm):
        #  if len(mat[x]) == 0: continue
        #  newl = []
        #  i = 0
        #  while i < len(mat[x]) - 1:
            #  if mat[x][i][0] == mat[x][i][1] and mat[x][i][1] == mat[x][i+1][0]:
                #  #  newl.append(mat[x][i][0], mat[x][i+1][0])

    #  inside = [[0] * maxm for i in range(maxm)]

    #  for x, allyl in enumerate(matx):
        #  for yl in allyl:
            #  for y in range(yl[0], yl[1]+1):
                #  inside[x][y] = 1

    #  for y, allxl in enumerate(maty):
        #  for xl in allxl:
            #  for x in range(xl[0], xl[1]+1):
                #  inside[x][y] = 1


    #  q = collections.deque([[sx, sy]])
    #  while q:
        #  x, y = q.popleft()
        #  #  if x < 0 or x >= maxm: continue
        #  #  if y < 0 or y >= maxm: continue
        #  if inside[x][y]:  continue

        #  inside[x][y] = 1
        #  q.append([x+1, y])
        #  q.append([x, y+1])
        #  q.append([x-1, y])
        #  q.append([x, y-1])
    #  print(inside)




    largest = []
    for i in range(len(red)):
        for j in range(i+1, len(red)):
            x1, x2 = min(red[i][0], red[j][0]), max(red[i][0], red[j][0])
            y1, y2 = min(red[i][1], red[j][1]), max(red[i][1], red[j][1])
            s = (x2 - x1 + 1) * (y2 - y1 + 1)
            largest.append((s, i, j))
    largest = sorted(largest, reverse = True)


    def check_crossing():
        for x, edge_ys, edge_ye in xedge:
            if x1 < x < x2:
                if not (edge_ys >= y2 or edge_ye <= y1):
                    return True
        for y, edge_xs, edge_xe in yedge:
            if y1 < y < y2:
                if not (edge_xs >= x2 or edge_xe <= x1):
                    return True

    for s, i, j in largest:
        x1, x2 = min(red[i][0], red[j][0]), max(red[i][0], red[j][0])
        y1, y2 = min(red[i][1], red[j][1]), max(red[i][1], red[j][1])
        #  print(s, x1, y1, x2, y2)

        if check_crossing():
            continue

        return s

        #  out = False
        #  for x in [x1, x2]:
            #  for y in range(y1+1, y2):
                #  for xl, xh in maty[y]:
                    #  if xl < x and xh > x:
                        #  #  print("out1")
                        #  out = True
                    #  if out: break
                #  if out: break
            #  if out: break

        #  if out: continue

        #  for y in [y1, y2]:
            #  for x in range(x1+1, x2):
                #  for yl, yh in matx[x]:
                    #  if yl < y and yh > y:
                        #  #  print("out2")
                        #  out = True
                    #  if out: break
                #  if out: break
            #  if out: break

        #  if out: continue
        #  return s

        #  if not inside[x1][y1]: continue
        #  if not inside[x1][y2]: continue
        #  if not inside[x2][y1]: continue
        #  if not inside[x2][y2]: continue



with open("tmp.txt") as f:
    #  f1(f)
    print(f2(f, 5, 4))
    pass

with open("9.txt") as f:
    #  f1(f)
    print(f2(f, 30000, 30000))
    pass
