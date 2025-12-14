import os

MOD = 100
def f1(f):
    s = 50
    c = 0
    for l in f:
        l = l.strip()
        di = l[0]
        st = int(l[1:])
        sgn = 1 if di == "R" else -1
        s += st * sgn
        if s % MOD == 0:
            c += 1
    print(c)
    pass

def f2(f):
    s = 50
    c = 0
    for l in f:
        l = l.strip()
        di = l[0]
        st = int(l[1:])
        sgn = 1 if di == "R" else -1
        if sgn > 0:
            s += st
            c += s // 100
        else:
            if s > 0 and s - st <= 0:
                c += 1
            s -= st
            if s < 0:
                c += abs(s) // 100
        s %= MOD
        print(l, c)
    print(c)
    pass

def main(f):
    #  f1(f)
    f2(f)


with open("1.txt") as f:
#  with open("tmp.txt") as f:
    main(f)
