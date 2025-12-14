import os

def f1(f):
    l_numbers = []
    for l in f:
        l = l.strip()
        l_numbers.append( [i for i in l.split()] )
    l_operators = l_numbers[-1]
    l_numbers = l_numbers[:-1]
    print(l_operators)
    results = 0
    for j, op in enumerate(l_operators):
        if op == "*":
            tmp = 1
            for l_num in l_numbers:
                tmp *= int(l_num[j])
        elif op == "+":
            tmp = 0
            for l_num in l_numbers:
                tmp += int(l_num[j])
        print(tmp)
        results += tmp

    print(results)
    pass

def f2(f):
    l_numbers = []
    for l in f:
        l = l[:-1]
        l_numbers.append(l)
    l_operators = l_numbers[-1].split()
    l_numbers = l_numbers[:-1]
    print(l_numbers, l_operators)
    iop = 0
    result = 0
    l_num_pro = []
    for j in range(len(l_numbers[0]) + 1):
        num = 0
        all_empty = True
        if j < len(l_numbers[0]):
            for i in range(len(l_numbers)):
                if l_numbers[i][j] != " ":
                    all_empty = False
                    num = num * 10 + int(l_numbers[i][j])
                    pass

        if all_empty:
            print(l_num_pro)
            if l_operators[iop] == "*":
                tmp = 1
                for num in l_num_pro:
                    tmp *= num
            elif l_operators[iop] == "+":
                tmp = 0
                for num in l_num_pro:
                    tmp += num
            result += tmp
            l_num_pro = []
            iop += 1
        else:
            l_num_pro.append(num)

    print(result)



def main(f):
    #  f1(f)
    f2(f)


with open("6.txt") as f:
#  with open("tmp.txt") as f:
    main(f)
