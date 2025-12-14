import os

def f1(f):
    fresh = []
    ing = []
    for l in f:
        l = l.strip()
        if "-" in l:
            x, y = l.split("-")
            fresh.append([int(x), int(y)])
        elif l:
            ing.append(int(l))

    sorted_fresh = []
    for x, y in sorted(fresh):
        if len(sorted_fresh) and x <= sorted_fresh[-1][1]:
            if y > sorted_fresh[-1][1]:
                sorted_fresh[-1][1] = y
        else:
            sorted_fresh.append([x, y])
    for x, y in sorted_fresh:
        print(x, y)

    j = 0
    good = 0
    for i in sorted(ing):
        # find the interval (or move past it)
        while j < len(sorted_fresh) and sorted_fresh[j][1] < i:
            j += 1
        # stopping
        if j >= len(sorted_fresh):
            break

        if sorted_fresh[j][0] <= i:
            good += 1
            print(i)
    print(good)

    sol2 = 0
    for x, y in sorted_fresh:
        sol2 += y - x + 1
    print(sol2)


            


def main(f):
    f1(f)


with open("5.txt") as f:
#  with open("tmp.txt") as f:
    main(f)
