import os

def f1(f):
    s = 0
    for l in f:
        l = l.strip()
        i1 = 0
        m1 = 0
        for i, c in enumerate(l):
            # find the c's i
            if m1 < int(c):
                i1 = i
                m1 = int(c)
        m2 = 0
        if i1 == len(l) - 1:
            # max is last, find the previous max
            for c in l[:-1]:
                m2 = max(m2, int(c))
            s += m2 * 10 + m1
        else:
            for c in l[i1 + 1:]:
                m2 = max(m2, int(c))
            s += m1 * 10 + m2
    print(s)

def f2(f):
    s = 0
    for l in f:
        l = l.strip()
        digit = 11
        left = -1
        s_line = 0
        #  while digit >= 0:
        for digit in range(11, -1, -1):
            m = 0
            for i in range(left + 1, len(l) - digit):
                if m < int(l[i]):
                    m = int(l[i])
                    left = i
            s_line = s_line * 10 + m
        print(s_line)
        s += s_line
    print(s)



    pass

def main(f):
    #  f1(f)
    f2(f)


with open("3.txt") as f:
#  with open("tmp.txt") as f:
    main(f)
