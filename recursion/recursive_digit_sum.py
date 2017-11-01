n, k = input().split()
n, k = [n, int(k)]


def super_digit(p, multiplication_flag):
    if len(p) == 1 and multiplication_flag is True:
        return p
    elif len(p) == 1 and multiplication_flag is False:
        multiplication_flag = True
        return super_digit(p * k, multiplication_flag)
    else:
        return super_digit(str(sum([int(i) for i in p])), multiplication_flag)


multiplier = False

print(super_digit(n, multiplier))
