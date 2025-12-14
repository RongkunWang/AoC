import os

def f1(s):
    res = 0
    for r in s.split(","):
        x, y = r.split('-')
        min_l = len(x)
        max_l = len(y)
        #  x, y = int(x), int(y)
        print(x, y)
        def get_sum(l, lower, upper):
            print(l, lower, upper)
            # l is the half length
            # upper is max value of the half-length (inclusive)
            res = (lower + upper) * (upper - lower + 1) // 2
            return res * (10 ** l + 1)


        for l in range(min_l, max_l + 1):
            # those are allowed full length
            if l % 2: continue
            # look at even length
            hl = l // 2
            # this is to be subtracted
            lower  = 10 ** (hl - 1)
            if l == min_l:
                first_half = int(x[:hl])
                second_half = int(x[hl:])
                if first_half < second_half:
                    lower = first_half + 1
                else:
                    lower = first_half
            higher = 10 ** hl - 1
            if l == max_l:
                first_half = int(y[:hl])
                second_half = int(y[hl:])
                higher = first_half
                if first_half > second_half:
                    higher -= 1
            tmp = get_sum(hl, lower, higher)
            res += tmp
            # I will remove the lower part so add it back
            #  if x[:hl] == x[hl:]:
                #  res += int(x)
            print("---> add", tmp)
    print(res)

def f2(s):
    res = 0
    for r in s.split(","):
        x, y = r.split('-')
        min_l = len(x)
        max_l = len(y)
        x = int(x)
        y = int(y)
        s_add = set()
        for l in range(1, max_l // 2 + 1):
            # l is partial length
            # number of repeats
            min_repeat = min_l // l
            max_repeat = max_l // l + 1

            # the min/max of this length
            l_min = 10 ** (l - 1)
            l_max = 10 ** l

            for repeat in range(min_repeat, max_repeat):
                if repeat == 1: continue
                for n in range(l_min, l_max):
                    val = int(str(n) * repeat)
                    if val > y: break
                    if val < x: continue
                    if val in s_add: continue
                    s_add.add(val)

                    res += val
                    print("---> add", val)
                    pass
    print(res)

def main(f):
    for l in f:
        #  f1(l.strip())
        f2(l.strip())


with open("2.txt") as f:
#  with open("tmp.txt") as f:
    main(f)
